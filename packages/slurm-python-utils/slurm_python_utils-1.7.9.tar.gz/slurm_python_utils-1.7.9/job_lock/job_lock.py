import abc, argparse, contextlib, datetime, itertools, logging, os, pathlib, random, re, socket, subprocess, sys, time, uuid
if sys.platform != "cygwin":
  import psutil

logger = logging.getLogger("JobLock")
logger.setLevel(logging.INFO)

def rm_missing_ok(path):
  if sys.version_info >= (3, 8):
    return path.unlink(missing_ok=True)
  else:
    try:
      return path.unlink()
    except FileNotFoundError:
      pass

def cpuid():
  node = uuid.getnode()
  #least significant bit of the first octet is not set --> this is a hardware address
  if not node & 2**40:
    return node

  #otherwise getnode gave us a random number!
  for filename in "/etc/machine-id", "/var/lib/dbus/machine-id", "/sys/class/dmi/id/product_uuid":
    try:
      with open(filename) as f:
        machineid = f.read().strip()
    except FileNotFoundError:
      continue
    return uuid.UUID(machineid).int

  if os.name == "nt":
    try:
      result = subprocess.run(
        ["wmic", "csproduct", "get", "uuid"],
        capture_output=True,
        text=True,
        check=True,
      )
      lines = result.stdout.strip().split('\n')
      for line in lines:
        line = line.strip()
        if not line: continue
        if line.lower() == "uuid": continue
        return uuid.UUID(line).int
    except (subprocess.CalledProcessError, ValueError):
      pass

  raise ValueError("Couldn't find a cpuid using any of the methods we know about")

class BatchSubmissionSystem(abc.ABC):
  def __init__(self):
    self.__knownrunningjobs = set()
    self.__joblistoutput = None
    self.__joblisterror = False

  class WrongBatchSystemError(Exception): pass
  class JobListCommandError(Exception): pass
  class InvalidJobListOutputError(Exception): pass

  @abc.abstractmethod
  def jobinfo(self): pass
  @abc.abstractmethod
  def joblistcommand(self, cpuid, jobid): pass
  @abc.abstractmethod
  def jobtype(self): pass
  @abc.abstractmethod
  def runningjobsfromoutput(self, output): pass
  @abc.abstractmethod
  def processjoblistcommanderror(self, calledprocesserror): pass

  def clearrunningjobscache(self):
    self.__knownrunningjobs.clear()
    self.__joblisterror = False

  def setjoblistoutput(self, *, output=None, filename=None):
    if filename is not None and output is not None:
      raise TypeError("Provided both output and filename")
    elif filename is not None:
      with open(filename, "rb") as f:
        self.setjoblistoutput(output=f.read())
    else:
      self.__joblistoutput = output

  def jobfinished(self, jobtype, cpuid, jobid, *, dojoblist=True, cachejoblist=True):
    if jobtype != self.jobtype():
      raise self.WrongBatchSystemError()
    logger.debug("Determining if job %s %s %s is finished", jobtype, cpuid, jobid)
    if self.__joblisterror: dojoblist = False
    joblistoutput = self.__joblistoutput

    if cachejoblist and (cpuid, jobid) in self.__knownrunningjobs:
      logger.debug("Job is already known to be running")
      return False #assume job is still running
    if not dojoblist and joblistoutput is None:
      logger.debug("Can't tell, because dojoblist is False and no output has been set")
      return None #don't know if the job finished

    if joblistoutput is not None:
      logger.debug("Using previously given job list output")
      output = joblistoutput
      freshjoblist = False
    else:
      try:
        output = subprocess.check_output(self.joblistcommand(cpuid, jobid), stderr=subprocess.STDOUT)
      except FileNotFoundError: #command doesn't exist on the batch machines
        logger.debug("Job list command doesn't exist")
        return None #we don't know if the job finished
      except subprocess.CalledProcessError as e:
        try:
          return self.processjoblistcommanderror(e)
        except self.JobListCommandError:
          logger.debug("Job list command gave an error")
          self.__joblisterror = True
          return None #we don't know if the job finished
        except subprocess.CalledProcessError:
          print(e.output.decode("ascii"), end="")
          raise
      freshjoblist = True

    try:
      runningjobs, pendingjobs = self.runningjobsfromoutput(output)
    except self.InvalidJobListOutputError:
      logger.debug("Job list command gave invalid output")
      return None #don't know if the job finished, probably a temporary glitch

    if not freshjoblist:
      runningjobs += pendingjobs
      pendingjobs = []

    maxseenjob = -float("inf"), -float("inf")
    for runningjob in runningjobs + pendingjobs:
      maxseenjob = max(runningjob, maxseenjob)

    for runningjob in runningjobs:
      self.__knownrunningjobs.add(runningjob)
      logger.debug("Job running: %s %s", cpuid, jobid)
      if runningjob == (cpuid, jobid):
        logger.debug("Found it!")
        return False #job is still running

    for pendingjob in pendingjobs:
      assert freshjoblist
      logger.debug("Job pending: %s %s", cpuid, jobid)
      if pendingjob == (cpuid, jobid):
        logger.debug("Found it!")
        return True #can happen if the job was cancelled and automatically resubmitted (happens on slurm, don't know about others)

    if not freshjoblist and (cpuid, jobid) > maxseenjob:
      logger.debug("Job list output was provided manually and the max seen job is %s, so we don't know if %s was submitted later", maxseenjob, (cpuid, jobid))
      return None #don't know if the job was started after the job list command was run

    logger.debug("Didn't find %s, so it must have finished", (cpuid, jobid))
    return True #job is finished

class Condor(BatchSubmissionSystem):
  @staticmethod
  def CONDOR_JOBINFO():
    if "_CONDOR_SCRATCH_DIR" not in os.environ: return None
    try:
      return os.environ["CONDOR_CLUSTERID"], os.environ["CONDOR_PROCID"]
    except KeyError:
      raise OSError("""Please put 'environment = "CONDOR_CLUSTERID=$(ClusterId) CONDOR_PROCID=$(ProcId)"' in your condor submission script""")
  def jobtype(self): return "CONDOR"
  def jobinfo(self):
    jobinfo = self.CONDOR_JOBINFO()
    if jobinfo is not None: return self.jobtype(), jobinfo[0], jobinfo[1]
    raise self.WrongBatchSystemError()

  def joblistcommand(self, cpuid, jobid):
    return ["condor_q", "-nobatch", "-run"]

  def processjoblistcommanderror(self, calledprocesserror):
    if b"Can't find address for schedd" in calledprocesserror.output:
      raise self.JobListCommandError(calledprocesserror)
    raise calledprocesserror

  def runningjobsfromoutput(self, output):
    running, pending = [], []
    for line in output.decode("ascii").split("\n"):
      line = line.strip()
      if not line: continue
      if line.startswith("-- Schedd:"): continue
      if line.startswith("ID "): continue
      jobid = line.split()[0]
      clusterid, procid = jobid.split(".")
      clusterid = int(clusterid)
      procid = int(procid)
      running.append((clusterid, procid))
    return running, pending

class Slurm(BatchSubmissionSystem):
  @staticmethod
  def SLURM_JOBID():
    return os.environ.get("SLURM_JOBID", None)
  def jobtype(self): return "SLURM"
  def jobinfo(self):
    jobid = self.SLURM_JOBID()
    if jobid is None: raise self.WrongBatchSystemError()
    return self.jobtype(), 0, jobid

  def joblistcommand(self, cpuid, jobid):
    return ["squeue", "--job", str(jobid), "--Format", "jobid,state", "--noheader"]

  def processjoblistcommanderror(self, calledprocesserror):
    if b"slurm_load_jobs error: Invalid job id specified" in calledprocesserror.output:
      return True #job is finished
    if b"slurm_load_jobs error: Unable to contact slurm controller (connect failure)" in calledprocesserror.output:
      raise self.JobListCommandError(calledprocesserror)
    if b"slurm_load_jobs error: Socket timed out on send/recv operation" in calledprocesserror.output:
      raise self.JobListCommandError(calledprocesserror)
    raise calledprocesserror

  def runningjobsfromoutput(self, output):
    running, pending = [], []
    for line in output.decode("ascii").split("\n"):
      line = line.strip()
      if not line: continue
      try:
        jobid, state = line.split()
      except ValueError:
        raise self.InvalidJobListOutputError()
      jobid = int(jobid)
      if state in ("PENDING", "PD"):
        pending.append((0, jobid))
      else:
        running.append((0, jobid))

    return running, pending

slurm = Slurm()
condor = Condor()
batchsubmissionsystems = [slurm, condor]

setsqueueoutput = slurm.setjoblistoutput
setcondorqoutput = condor.setjoblistoutput

def jobinfo():
  for system in batchsubmissionsystems:
    try:
      return system.jobinfo()
    except BatchSubmissionSystem.WrongBatchSystemError:
      pass
  return sys.platform, cpuid(), os.getpid()

class JobLock(object):
  defaulttimeout = datetime.timedelta(days=7)
  defaultcorruptfiletimeout = datetime.timedelta(hours=1)
  defaultminimumtimeforiterativelocks = datetime.timedelta(seconds=10)
  copyspeedlowerlimitbytespersecond = 1e6  #1 MBps

  def __init__(self, filename, *, outputfiles=[], checkoutputfiles=True, inputfiles=[], checkinputfiles=True, prevsteplockfiles=[], timeout=None, corruptfiletimeout=None, minimumtimeforiterativelocks=None, mkdir=False, dosqueue=True, cachesqueue=True, suppressfileopenfailure=False):
    self.filename = pathlib.Path(filename)
    self.outputfiles = [pathlib.Path(_) for _ in outputfiles]
    self.inputfiles = [pathlib.Path(_) for _ in inputfiles]
    self.prevsteplockfiles = [pathlib.Path(_) for _ in prevsteplockfiles]
    self.checkoutputfiles = outputfiles and checkoutputfiles
    self.checkinputfiles = inputfiles and checkinputfiles
    self.checkprevsteplockfiles = prevsteplockfiles
    self.removed_failed_job = False

    if timeout is None:
      timeout = self.defaulttimeout
    self.timeout = timeout

    if corruptfiletimeout is None:
      corruptfiletimeout = self.defaultcorruptfiletimeout
    self.corruptfiletimeout = corruptfiletimeout

    if minimumtimeforiterativelocks is None:
      minimumtimeforiterativelocks = self.defaultminimumtimeforiterativelocks
    self.minimumtimeforiterativelocks = minimumtimeforiterativelocks

    self.mkdir = mkdir
    self.dosqueue = dosqueue
    self.cachesqueue = cachesqueue
    self.suppressfileopenfailure = suppressfileopenfailure
    self.sublockkwargs = {
      "checkoutputfiles": checkoutputfiles,
      "checkinputfiles": checkinputfiles,
      "mkdir": mkdir,
      "dosqueue": dosqueue,
      "cachesqueue": cachesqueue,
      "timeout": timeout,
      "corruptfiletimeout": corruptfiletimeout,
      "minimumtimeforiterativelocks": minimumtimeforiterativelocks,
      "suppressfileopenfailure": True,
    }
    self.__reset()

  def __reset(self):
    self.fd = self.f = None
    self.bool = False
    self.__inputsexist = self.__outputsexist = self.__prevsteplockfilesexist = self.__oldjobinfo = self.__iterative_lock = None

  @property
  def wouldbevalid(self):
    if self: return True
    with self:
      return bool(self)

  def runningjobinfo(self, *, exceptions=False):
    try:
      with open(self.filename) as f:
        contents = f.read()
        firstline = contents.split("\n")[0]
        jobtype, cpuid, jobid = firstline.split()
        cpuid = int(cpuid)
        jobid = int(jobid)
        return jobtype, cpuid, jobid
    except (IOError, OSError, ValueError):
      if exceptions: raise
      return None, None, None

  @property
  def outputsexist(self):
    return self.__outputsexist

  @property
  def inputsexist(self):
    return self.__inputsexist

  @property
  def prevsteplockfilesexist(self):
    return self.__prevsteplockfilesexist

  @property
  def oldjobinfo(self):
    return self.__oldjobinfo

  @property
  def iterative_lock(self):
    return self.__iterative_lock
  @property
  def iterative_lock_debuginfo(self):
    if self.iterative_lock is None: return None
    return self.iterative_lock.debuginfo

  def __open(self):
    self.fd = os.open(self.filename, os.O_CREAT | os.O_EXCL | os.O_WRONLY)

  @property
  def lock_iteration_number(self):
    match = re.match("[.]lock(?:_([0-9]+))?$", self.filename.suffix)
    if match:
      n = match.group(1)
      if n is None: n = 1
      return int(n)
    else:
      return 0

  @property
  def iterative_lock_filename(self):
    n = self.lock_iteration_number
    if n == 0:
      return self.filename.with_suffix(self.filename.suffix+".lock")
    else:
      #sleep by a random amount less than 1/100 of a second to lower the probability of two jobs competing indefinitely
      time.sleep(random.random()/100)
      return self.filename.with_suffix(f".lock_{n+1}")

  def clean_up_iterative_locks(self):
    iterative_lock_filename = self.iterative_lock_filename

    def n_from_filename(filename):
      match = re.match("[.]lock(?:_([0-9]+))?$", filename.suffix)
      if not match: return -float("inf")
      n = match.group(1)
      if n is None: n = 1
      return int(n)

    my_n = n_from_filename(iterative_lock_filename)-1
    if my_n > 1: return #they'll be cleaned up when the non-iterative version cleans them up

    filenames = iterative_lock_filename.parent.glob(iterative_lock_filename.with_suffix(".lock").name+"*")
    filenames = [_ for _ in filenames if n_from_filename(_) > my_n]
    if not filenames: return
    filenames.sort(key=n_from_filename, reverse=True)

    with JobLock(self.filename.with_suffix(".cleanup.lock"), **self.sublockkwargs) as lock:
      if not lock: return
      for filename in filenames:
        with JobLock(filename, **self.sublockkwargs) as lock:
          if not lock:
            break

  def __enter__(self):
    self.removed_failed_job = False
    if self.checkoutputfiles and not self.filename.exists():
      self.__outputsexist = {_: _.exists() for _ in self.outputfiles}
      if all(self.outputsexist.values()):
        self.clean_up_iterative_locks()
        return self
    if self.checkinputfiles:
      self.__inputsexist = {_: _.exists() for _ in self.inputfiles}
      if not all(self.inputsexist.values()):
        return self
    if self.checkprevsteplockfiles:
      self.__prevsteplockfilesexist = {_: not JobLock(_, **self.sublockkwargs).wouldbevalid for _ in self.prevsteplockfiles}
      if any(self.prevsteplockfilesexist.values()):
        return self
    if self.mkdir:
      self.filename.parent.mkdir(parents=True, exist_ok=True)
    try:
      self.__open()
    except (FileExistsError, PermissionError) as e:
      #PermissionError can happen because we actually don't have permissions
      #or because of network connectivity issues.
      #If the former, we want to raise the error.
      #If the latter, we want to wait a bit and retry.
      #There's not really a way to distinguish, other than that network connectivity
      #issues should only be intermittent.
      if isinstance(e, PermissionError):
        if self.lock_iteration_number > 5:
          raise
        else:
          logger.warning(f"PermissionError when creating {self.filename}, waiting 1 second and retrying... ({self.lock_iteration_number}/5)")
          time.sleep(1)
      try:
        modified = datetime.datetime.fromtimestamp(self.filename.stat().st_mtime)
      except (FileNotFoundError, PermissionError):
        age = None
      else:
        now = datetime.datetime.now()
        age = now - modified
      if age is not None and self.minimumtimeforiterativelocks is not None and age < self.minimumtimeforiterativelocks:
        return self
      #check if the job died without removing the lock
      #however this needs another job lock, because it has
      #a race condition: two jobs could be looking if the previous
      #job failed at the same time, and one of them could remove
      #the lock created by the other one
      try:
        with JobLock(self.iterative_lock_filename, **self.sublockkwargs) as iterative_lock:
          self.__iterative_lock = iterative_lock
          if not iterative_lock: return self
          try:
            self.__oldjobinfo = self.runningjobinfo(exceptions=True)
          except (IOError, OSError) as e:
            self.__oldjobinfo = e
            try:
              self.__open()
            except (FileExistsError, PermissionError):
              return self
          except ValueError as e:
            self.__oldjobinfo = e
            if age is not None and (self.corruptfiletimeout is not None and age >= self.corruptfiletimeout or self.timeout is not None and age >= self.timeout):
              for outputfile in self.outputfiles:
                rm_missing_ok(outputfile)
              rm_missing_ok(self.filename)
              self.removed_failed_job = True
              try:
                self.__open()
              except (FileExistsError, PermissionError):
                return self
            else:
              if age is not None and age >= datetime.timedelta(seconds=1):
                logger.warning(f"{self.filename} is likely corrupt (age {age}), consider setting a corrupt file timeout to remove it")
              return self
          else:
            if age is not None and self.timeout is not None and age >= self.timeout or jobfinished(*self.oldjobinfo, dojoblist=self.dosqueue, cachejoblist=self.cachesqueue):
              for outputfile in self.outputfiles:
                rm_missing_ok(outputfile)
              rm_missing_ok(self.filename)
              self.removed_failed_job = True
              try:
                self.__open()
              except (FileExistsError, PermissionError):
                return self
            else:
              return self
      except RecursionError:
        return self
    except FileNotFoundError:
      if self.suppressfileopenfailure and self.filename.parent.exists():
        return self
      else:
        raise

    self.f = os.fdopen(self.fd, 'w')

    message = " ".join(str(_) for _ in jobinfo())
    message += "\n" + socket.gethostname()
    try:
      self.f.write(message+"\n")
    except (IOError, OSError):
      pass
    try:
      self.f.close()
    except (IOError, OSError):
      pass
    self.bool = True
    return self

  def __exit__(self, exc_type, exc, traceback):
    if self:
      #clean up output files if job failed
      if exc is not None:
        for outputfile in self.outputfiles:
          rm_missing_ok(outputfile)
      #clean up iterative locks whose jobs died
      self.clean_up_iterative_locks()
      #remove this lock file
      rm_missing_ok(self.filename)
    self.__reset()

  def __bool__(self):
    return self.bool

  @property
  def debuginfo(self):
    return {
      "outputsexist": self.outputsexist,
      "inputsexist": self.inputsexist,
      "prevsteplockfilesexist": self.prevsteplockfilesexist,
      "oldjobinfo": self.oldjobinfo,
      "removed_failed_job": self.removed_failed_job,
      "iterative_lock_debuginfo": self.iterative_lock_debuginfo,
    }

  @classmethod
  def setdefaultcorruptfiletimeout(cls, timeout):
    cls.defaultcorruptfiletimeout = timeout
  @classmethod
  def setdefaulttimeout(cls, timeout):
    cls.defaulttimeout = timeout
  @classmethod
  def setdefaultminimumtimeforiterativelocks(cls, timeout):
    cls.defaultminimumtimeforiterativelocks = timeout

def clear_running_jobs_cache():
  for system in batchsubmissionsystems:
    system.clearrunningjobscache()

def jobfinished(jobtype, cpuid, jobid, *, dojoblist=True, cachejoblist=True):
  for system in batchsubmissionsystems:
    try:
      return system.jobfinished(jobtype=jobtype, cpuid=cpuid, jobid=jobid, dojoblist=dojoblist, cachejoblist=cachejoblist)
    except BatchSubmissionSystem.WrongBatchSystemError:
      pass

  else:
    myjobtype, mycpuid, myjobid = jobinfo()
    if myjobtype != jobtype: return None #we don't know if the job finished
    if mycpuid != cpuid: return None #we don't know if the job finished
    if jobid == myjobid: return False #job is still running
    if sys.platform == "cygwin":
      psoutput = subprocess.check_output(["ps", "-s"])
      lines = psoutput.split(b"\n")
      for line in lines[1:]:
        if not line: continue
        if int(line.split(maxsplit=1)[0]) == jobid:
          return False #job is still running
      return True #job is finished
    else:
      for process in psutil.process_iter():
        if jobid == process.pid:
          return False #job is still running
      return True #job is finished

class JobLockAndWait(JobLock):
  defaultsilent = False

  def __init__(self, name, delay, *, printmessage=None, task="doing this", maxiterations=1000, silent=None, waitforinputs=False, **kwargs):
    super().__init__(name, **kwargs)
    self.delay = delay
    if printmessage is None:
      printmessage = f"Another process is already {task}.  Waiting {delay} seconds."
    self.__printmessage = printmessage
    if silent is None:
      silent = self.defaultsilent
    self.__silent = silent
    self.__waitforinputs = waitforinputs
    self.niterations = 0
    self.maxiterations = maxiterations

  def __enter__(self):
    for self.niterations in itertools.count(1):
      if self.niterations > self.maxiterations:
        raise RuntimeError(f"JobLockAndWait still did not succeed after {self.maxiterations} iterations")
      result = super().__enter__()
      if result:
        return result
      elif self.checkoutputfiles and self.outputsexist is not None and all(self.outputsexist.values()):
        return result
      elif self.checkinputfiles and self.inputsexist is not None:
        missinginputs = [k for k, v in self.inputsexist.items() if not v]
        if missinginputs:
          message = f"Some input files are missing: {', '.join(str(_) for _ in missinginputs)}."
          if self.__waitforinputs:
            if not self.__silent: print(f"{message} Waiting {self.delay} seconds.")
          else:
            raise FileNotFoundError(message)
      else:
        if not self.__silent: print(self.__printmessage)
      time.sleep(self.delay * (1 + 0.1 * (random.random() - 0.5)))

def clean_up_old_job_locks(*folders, glob="*.lock_*", howold=datetime.timedelta(days=7), dryrun=False, silent=False):
  for folder in folders:
    folder = pathlib.Path(folder)
    all_locks = sorted(folder.rglob(glob))
    all_first_order_locks = sorted({filename.with_suffix(filename.suffix.split("_")[0]) for filename in all_locks})
    locks_dict = {first_order_lock: {lock for lock in all_locks if lock.with_suffix(lock.suffix.split("_")[0]) == first_order_lock} for first_order_lock in all_first_order_locks}

    remove = []
    dontremove = []
    for first_order_lock_file, lock_files in sorted(locks_dict.items()):
      try:
        modified = max(datetime.datetime.fromtimestamp(file.stat().st_mtime) for file in lock_files)
      except FileNotFoundError:
        dontremove.append(first_order_lock_file)
        continue
      now = datetime.datetime.now()
      if now - modified < howold:
        dontremove.append(first_order_lock_file)
      else:
        remove.append(first_order_lock_file)

    if dryrun:
      verb = "Would remove"
      dontverb = "Would not remove"
    else:
      verb = "Removing"
      dontverb = "Keeping"

    if silent:
      def doprint(*args, **kwargs): pass
    else:
      doprint = print

    doprint(f"{verb} the following locks (and their iterations):")
    for _ in remove:
      doprint(_)
      if not dryrun:
        with JobLock(_, corruptfiletimeout=howold): pass
    doprint(f"{dontverb} the following locks (and their iterations):")
    for _ in dontremove: doprint(_)

def clean_up_old_job_locks_argparse(args=None):
  p = argparse.ArgumentParser()
  p.add_argument("folders", type=pathlib.Path, nargs="+", metavar="folder")
  p.add_argument("--glob", default="*.lock_*")
  p.add_argument("--hours-old", type=lambda x: datetime.timedelta(hours=float(x)), default=datetime.timedelta(days=7), dest="howold")
  p.add_argument("--dry-run", dest="dryrun", action="store_true")
  p.add_argument("--silent", action="store_true")
  args = p.parse_args(args=args)
  folders = args.__dict__.pop("folders")
  return clean_up_old_job_locks(*folders, **args.__dict__)

class MultiJobLock(contextlib.ExitStack):
  """
  JobLock with multiple files.
  If any of them fail, all the ones that previously succeeded are closed
  and the whole thing is considered to fail.
  """
  def __init__(self, *filenames, **kwargs):
    super().__init__()
    self.__filenames = filenames
    self.__kwargs = kwargs

  def __enter__(self):
    super().__enter__()
    for filename in self.__filenames:
      if not self.enter_context(JobLock(filename, **self.__kwargs)):
        self.close()
        return False
    return True

def add_job_lock_arguments(argumentparser):
  p = argumentparser
  g = p.add_mutually_exclusive_group()
  g.add_argument("--squeue-output", help="output of 'squeue --Format jobid,state --noheader'")
  g.add_argument("--squeue-output-file", type=pathlib.Path, help="file containing the output of 'squeue --Format jobid,state --noheader'")
  g = p.add_mutually_exclusive_group()
  g.add_argument("--condorq-output", help="output of 'condor_q -nobatch'")
  g.add_argument("--condorq-output-file", type=pathlib.Path, help="file containing the output of 'condor_q -nobatch'")

  def parsetimedelta(s):
    regex = r"(?P<hours>\d+):(?P<minutes>\d+):(?P<seconds>\d+(?:\.\d*)?)$"
    match = re.match(regex, s)
    if match is None:
      raise ValueError(f"{s} does not match {regex}")
    return datetime.timedelta(hours=int(match.group("hours")), minutes=int(match.group("minutes")), seconds=float(match.group("seconds")))
  p.add_argument("--job-lock-timeout", type=parsetimedelta, help=f"delete joblock files after this long (%%H:%%M:%%S, default {JobLock.defaulttimeout})")
  p.add_argument("--corrupt-job-lock-timeout", type=parsetimedelta, help=f"delete corrupt joblock files after this long (%%H:%%M:%%S, default {JobLock.defaultcorruptfiletimeout})")
  p.add_argument("--minimum-time-for-iterative-locks", type=parsetimedelta, help=f"if the lock has existed for at least this long, check if the job is still running and, if not, delete the lock (%%H:%%M:%%S, default {JobLock.defaultminimumtimeforiterativelocks})")

def process_job_lock_arguments(parsed_args):
  dct = parsed_args.__dict__
  setsqueueoutput(output=dct.pop("squeue_output"), filename=dct.pop("squeue_output_file"))
  setcondorqoutput(output=dct.pop("condorq_output"), filename=dct.pop("condorq_output_file"))

  timeout = dct.pop("corrupt_job_lock_timeout")
  JobLock.setdefaultcorruptfiletimeout(timeout)
  timeout = dct.pop("minimum_time_for_iterative_locks")
  JobLock.setdefaultminimumtimeforiterativelocks(timeout)
  timeout = dct.pop("job_lock_timeout")
  JobLock.setdefaulttimeout(timeout)
