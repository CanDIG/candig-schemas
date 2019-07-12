"""
Utilities used across many CanDIG packages
"""
import io
import contextlib
import fnmatch
import functools
import humanize
import itertools
import os
import shlex
import signal
import subprocess
import sys
import time
import yaml


def log(message):
    """
    Log a message
    """
    print(message)


def getPathOfExecutable(executable):
    """
    Returns the full path of the executable, or None if the executable
    can not be found.
    """
    exe_paths = os.environ['PATH'].split(':')
    for exe_path in exe_paths:
        exe_file = os.path.join(exe_path, executable)
        if os.path.isfile(exe_file) and os.access(exe_file, os.X_OK):
            return exe_file
    return None


def requireExecutables(executables):
    """
    Check that all of the given executables are on the path.
    If at least one of them is not, exit the script and inform
    the user of the missing requirement(s).
    """
    missingExecutables = []
    for executable in executables:
        if getPathOfExecutable(executable) is None:
            missingExecutables.append(executable)
    if len(missingExecutables) > 0:
        log("In order to run this script, the following "
            "executables need to be on the path:")
        for missingExecutable in missingExecutables:
            log(missingExecutable)
        exit(1)


def runCommand(command, silent=False, shell=False):
    """
    Run a shell command
    """
    splits = shlex.split(command)
    runCommandSplits(splits, silent=silent, shell=shell)


def runCommandReturnOutput(cmd):
    """
    Runs a shell command and return the stdout and stderr
    """
    splits = shlex.split(cmd)
    proc = subprocess.Popen(
        splits, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    if proc.returncode != 0:
        raise subprocess.CalledProcessError(stdout, stderr)
    return stdout, stderr


def runCommandSplits(splits, silent=False, shell=False):
    """
    Run a shell command given the command's parsed command line
    """
    try:
        if silent:
            with open(os.devnull, 'w') as devnull:
                subprocess.check_call(
                    splits, stdout=devnull, stderr=devnull, shell=shell)
        else:
            subprocess.check_call(splits, shell=shell)
    except OSError as exception:
        if exception.errno == 2:  # cmd not found
            raise Exception(
                "Can't find command while trying to run {}".format(splits))
        else:
            raise


def getAuthValues(filePath='scripts/auth.yml'):
    """
    Return the script authentication file as a dictionary
    """
    return getYamlDocument(filePath)


def getYamlDocument(filePath):
    """
    Return a yaml file's contents as a dictionary
    """
    with open(filePath) as stream:
        doc = yaml.load(stream)
        return doc


def captureOutput(func, *args, **kwargs):
    """
    Runs the specified function and arguments, and returns the
    tuple (stdout, stderr) as strings.
    """
    stdout = sys.stdout
    sys.stdout = io.StringIO()
    stderr = sys.stderr
    sys.stderr = io.StringIO()
    try:
        func(*args, **kwargs)
        stdoutOutput = sys.stdout.getvalue()
        stderrOutput = sys.stderr.getvalue()
    finally:
        sys.stdout.close()
        sys.stdout = stdout
        sys.stderr.close()
        sys.stderr = stderr
    return stdoutOutput, stderrOutput


def zipLists(*lists):
    """
    Checks to see if all of the lists are the same length, and throws
    an AssertionError otherwise.  Returns the zipped lists.
    """
    length = len(lists[0])
    for i, list_ in enumerate(lists[1:]):
        if len(list_) != length:
            msg = "List at index {} has length {} != {}".format(
                i + 1, len(list_), length)
            raise AssertionError(msg)
    return list(zip(*lists))


def getLinesFromLogFile(stream):
    """
    Returns all lines written to the passed in stream
    """
    stream.flush()
    stream.seek(0)
    lines = stream.readlines()
    return lines


def powerset(iterable, maxSets=None):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)

    See https://docs.python.org/2/library/itertools.html#recipes
    """
    s = list(iterable)
    return itertools.islice(itertools.chain.from_iterable(
        itertools.combinations(s, r) for r in range(len(s) + 1)),
        0, maxSets)


def chomp(line):
    """
    Returns a string stripped of its trailing newline character
    """
    assert line[-1] == '\n'
    return line[:-1]


def getFilePathsWithExtensionsInDirectory(dirTree, patterns, sort=True):
    """
    Returns all file paths that match any one of patterns in a
    file tree with its root at dirTree.  Sorts the paths by default.
    """
    filePaths = []
    for root, dirs, files in os.walk(dirTree):
        for filePath in files:
            for pattern in patterns:
                if fnmatch.fnmatch(filePath, pattern):
                    fullPath = os.path.join(root, filePath)
                    filePaths.append(fullPath)
                    break
    if sort:
        filePaths.sort()
    return filePaths


def touch(filepath):
    """
    Creates an empty file at filepath, if it does not already exist
    """
    with open(filepath, 'a'):
        pass


def assertFileContentsIdentical(pathOne, pathTwo):
    with open(pathOne) as fileOne, open(pathTwo) as fileTwo:
        for i, (lineOne, lineTwo) in enumerate(zip(fileOne, fileTwo)):
            if lineOne != lineTwo:
                msg = "Mismatch on line {}: '{}' != '{}'".format(
                    i + 1, lineOne, lineTwo)
                raise AssertionError(msg)
        # one file could have more lines than the other file
        extraLine = fileOne.readline()
        if extraLine:
            msg = "File one has extra line: '{}'".format(extraLine)
            raise AssertionError(msg)
        extraLine = fileTwo.readline()
        if extraLine:
            msg = "File two has extra line: '{}'".format(extraLine)
            raise AssertionError(msg)


# ---------------- Decorators ----------------


class TimeoutException(Exception):
    """
    A process has taken too long to execute
    """


class Timed(object):
    """
    Decorator that times a method, reporting runtime at finish
    """
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self.start = time.time()
            result = func(*args, **kwargs)
            self.end = time.time()
            self._report()
            return result
        return wrapper

    def _report(self):
        delta = self.end - self.start
        timeString = humanize.time.naturaldelta(delta)
        log("Finished in {} ({:.2f} seconds)".format(timeString, delta))


class Repeat(object):
    """
    A decorator to use for repeating a tagged function.
    The tagged function should return true if it wants to run again,
    and false if it wants to stop repeating.
    """
    defaultSleepSeconds = 0.1

    def __init__(self, sleepSeconds=defaultSleepSeconds):
        self.sleepSeconds = sleepSeconds

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            while func(*args, **kwargs):
                time.sleep(self.sleepSeconds)
        return wrapper


class Timeout(object):
    """
    A decorator to use for only allowing a function to run
    for a limited amount of time
    """
    defaultTimeoutSeconds = 60

    def __init__(self, timeoutSeconds=defaultTimeoutSeconds):
        self.timeoutSeconds = timeoutSeconds

    def __call__(self, func):

        def _handle_timeout(signum, frame):
            raise TimeoutException()

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # set the alarm and execute func
                signal.signal(signal.SIGALRM, _handle_timeout)
                signal.alarm(self.timeoutSeconds)
                result = func(*args, **kwargs)
            finally:
                # clear the alarm
                signal.alarm(0)
            return result
        return wrapper


# ---------------- Context managers ----------------


@contextlib.contextmanager
def suppressOutput():
    # I would like to use sys.stdout.fileno() and sys.stderr.fileno()
    # here instead of literal fd numbers, but nose does something like
    # sys.stdout = StringIO.StringIO() when the -s flag is not enabled
    # (to capture test output so it doesn't get entangled with nose's
    # display) so the sys.stdout and sys.stderr objects are not able to
    # be accessed here.
    try:
        # redirect stdout and stderr to /dev/null
        devnull = open(os.devnull, 'w')
        origStdoutFd = 1
        origStderrFd = 2
        origStdout = os.dup(origStdoutFd)
        origStderr = os.dup(origStderrFd)
        sys.stdout.flush()
        sys.stderr.flush()
        os.dup2(devnull.fileno(), origStdoutFd)
        os.dup2(devnull.fileno(), origStderrFd)
        # enter the wrapped code
        yield
    finally:
        # restore original file streams
        devnull.flush()
        os.dup2(origStdout, origStdoutFd)
        os.dup2(origStderr, origStderrFd)
        # clean up
        os.close(origStdout)
        os.close(origStderr)
        devnull.close()


@contextlib.contextmanager
def performInDirectory(dirPath):
    """
    Change the current working directory to dirPath before performing
    an operation, then restore the original working directory after
    """
    originalDirectoryPath = os.getcwd()
    try:
        os.chdir(dirPath)
        yield
    finally:
        os.chdir(originalDirectoryPath)
