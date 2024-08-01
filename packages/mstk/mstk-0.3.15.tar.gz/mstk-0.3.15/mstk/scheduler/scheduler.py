import datetime
import os
import time
from mstk import logger
from mstk.misc import DocstringMeta
from .pbsjob import PbsJob


class Scheduler(metaclass=DocstringMeta):
    '''
    Base class for job schedulers.

    Scheduler should not be constructed directly. Use its subclasses instead.

    Attributes
    ----------
    queue : str
        The jobs will be submitted to this queue.
    n_proc : int
        The CPU cores a job can use.
    n_gpu : int
        The GPU card a job can use.
    env_cmd : str, Optional
        The commands for setting up the environment before running real calculations.
    sh : str
        The default name of the job script
    max_running_hour: int
        The wall time limit for a job in hours.
    username : str
        The current user
    cached_jobs_expire : int
        The lifetime of cached jobs in seconds.
    '''

    #: Whether this is a remote job scheduler
    is_remote = False

    def __init__(self, queue=None, n_proc=1, n_gpu=0, env_cmd=None):
        self.queue = queue
        self.n_proc = n_proc
        self.n_gpu = n_gpu
        self.env_cmd = env_cmd or ''
        self.remote_dir = None

        if os.name == 'nt':
            import win32api
            self.username = win32api.GetUserName()
        else:
            import pwd
            self.username = pwd.getpwuid(os.getuid()).pw_name

        self.max_running_hour = 24
        self.sh = '_job.sh'
        self.cached_jobs_expire = 60  # seconds
        self._cached_jobs = []
        self._cache_last_update = None

    def is_working(self):
        '''
        Whether this job scheduler is running normally.

        Returns
        -------
        is : bool
        '''
        raise NotImplementedError('This method should be implemented by subclasses')

    def generate_sh(self, commands, name, workdir=None, sh=None):
        '''
        Generate a shell script for commands to be executed by the job scheduler on compute nodes.

        Parameters
        ----------
        commands : str
            List of commands to be executed by the job scheduler on compute node step by step.
        name : str
            The name of the job to be submitted.
        workdir : str, Optional
            The working directory.
        sh : str
            The name (path) of the shell script being written.
            If not set, will use the default :attr:`sh`.
        '''
        raise NotImplementedError('This method should be implemented by subclasses')

    def upload(self, **kwargs) -> bool:
        '''
        Upload the simulation files to target folder.

        This method should be implemented by subclasses that is remote scheduler,
        which is determined by the attribute :attr:`is_remote`.
        If it's not a remote job scheduler, will simply return True.

        Returns
        -------
        successful : bool
            Whether the upload is successful
        '''
        pass

    def download(self, **kwargs) -> bool:
        '''
        Download the simulation files to target folder.

        This method should be implemented by subclasses that is remote scheduler,
        which is determined by the attribute :attr:`is_remote`.
        If it's not a remote job scheduler, will simply return True.

        Returns
        -------
        successful : bool
            Whether the download is successful
        '''
        pass

    def submit(self, sh=None, **kwargs):
        '''
        Submit a job script to scheduler.

        Parameters
        ----------
        sh : str, optional
            The file name of the job script.
            If not set, will use the default :attr:`sh`.

        Returns
        -------
        id : int
            Job ID. -1 means failed
        '''
        raise NotImplementedError('This method should be implemented by subclasses')

    def get_job_from_name(self, name):
        '''
        Get the job with specified name.

        If such a job can not be found, None will be returned.
        If several job have same name, the most recently submitted one will be returned.

        Parameters
        ----------
        name : str

        Returns
        -------
        job : PbsJob or None
        '''
        # if several job have same name, return the one with the largest id (most recent job)
        for job in sorted(self.get_jobs(), key=lambda x: x.id, reverse=True):
            if job.name == name:
                return job
        return None

    def is_running(self, name):
        '''
        Check whether a job is pending or running (not killed or finished or failed).

        Parameters
        ----------
        name : str

        Returns
        -------
        is : bool
        '''
        job = self.get_job_from_name(name)
        if job is None:
            return False
        return job.state in [PbsJob.State.PENDING, PbsJob.State.RUNNING]

    def kill_job(self, name):
        '''
        Kill a job which has the specified name.

        Parameters
        ----------
        name : str

        Returns
        -------
        killed : bool
        '''
        raise NotImplementedError('This method should be implemented by subclasses')

    def get_jobs(self, use_cache=True):
        '''
        Retrieve all the jobs that are currently managed by job scheduler.

        It calls `scontrol show job` for Slurm or `qstat -f -u` for Torque to get the list of jobs.
        If some jobs have finished long time ago (depends on the setting of job scheduler on the machine),
        they may disappear from the list output by job scheduler.

        In order not to apply too much pressure to the job scheduler, cache can be used to stores the jobs.
        If `use_cache` set to True and the cache is not expired, this method will return the cached results without calling `scontrol` or `qstat`.
        The lifetime of cache is determined by attribute :attr:`cached_jobs_expire` in seconds.

        Parameters
        ----------
        use_cache : bool
            Whether the cached job list be used

        Returns
        -------
        jobs : list of PbsJob
        '''
        if not use_cache or \
                self._cache_last_update is None \
                or (datetime.datetime.now() - self._cache_last_update).total_seconds() >= self.cached_jobs_expire:
            logger.info('Updating job information...')
            self._cached_jobs = []
            jobs = []
            for i in [3, 2, 1]:
                # in case _get_jobs() raise Exception
                try:
                    jobs = self._get_jobs()
                except Exception as e:
                    logger.warning(repr(e))
                if jobs:
                    break
                # in case _get_jobs() failed, retry after 1s
                if i > 1:
                    time.sleep(1)
            for job in reversed(jobs):  # reverse the job list, in case jobs with same name
                if job not in self._cached_jobs:
                    self._cached_jobs.append(job)

            self._cached_jobs.reverse()  # reverse the job list
            self._cache_last_update = datetime.datetime.now()

        return self._cached_jobs

    def _get_jobs(self):
        '''
        Retrieve all the jobs that are currently managed by job scheduler.

        It calls `scontrol show job` for Slurm or `qstat -f -u` for Torque to get the list of jobs.
        If some jobs have finished long max_running_hour ago (depends on the setting of job scheduler on the machine),
        they may disappear from the list outputted by job scheduler.

        Returns
        -------
        jobs : list of PbsJob
        '''
        raise NotImplementedError('This method should be implemented by subclasses')

    @property
    def n_running_jobs(self) -> int:
        '''
        The number of jobs that is currently pending or running (not killed or finished or failed)

        Only the jobs belongs to the specified :attr:`queue` will be considered.
        This method does not use cached job list. Don't call it often.

        Returns
        -------
        n : int
        '''
        n = 0
        for job in self.get_jobs(use_cache=False):
            if job.state != PbsJob.State.DONE and job.queue == self.queue:
                n += 1
        return n
