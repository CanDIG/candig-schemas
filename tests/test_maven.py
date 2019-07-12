"""
Runs the maven tests
"""

import shlex
import subprocess
import unittest

import utils


@unittest.skip("Disabled, unused")
class TestMaven(unittest.TestCase):
    """
    Uses maven to run tests
    """
    def testMaven(self):
        # ensure the maven tests don't fail or issue warnings
        mvnInstall = \
            "mvn install -DskipTests=true -Dmaven.javadoc.skip=true -B -V"
        self.runCommandCheckWarnings(mvnInstall)
        mvnTest = "mvn test -B"
        self.runCommandCheckWarnings(mvnTest)

    def runCommandCheckWarnings(self, cmd):
        utils.log("Running '{}'".format(cmd))
        splits = shlex.split(cmd)
        output = subprocess.check_output(splits).decode('utf-8').split('\n')
        self.ensureNoWarnings(output, cmd)

    def ensureNoWarnings(self, lines, streamName):
        pattern = '[WARNING]'
        matchingLines = []
        for line in lines:
            if pattern in line:
                matchingLines.append(line[:-1])
        if len(matchingLines) != 0:
            raise Exception("warning(s) detected in {}:\n{}".format(
                streamName, '\n'.join(matchingLines)))
