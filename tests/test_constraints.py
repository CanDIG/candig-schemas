"""
Tests the constraints invariants
"""

import unittest

import ga4gh.common.utils as utils


class TestConstraints(unittest.TestCase):

    constraintsFilePath = 'python/constraints.txt'
    constraintsFileDefaultPath = 'python/constraints.txt.default'

    def testDefault(self):
        utils.assertFileContentsIdentical(
            self.constraintsFilePath, self.constraintsFileDefaultPath)
