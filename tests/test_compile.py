"""
Tests the schema compilation
"""

import os
import tempfile
import unittest
import utils
import candig.schemas._version as version  # NOQA


class TestCompile(unittest.TestCase):

    def _getDirAndFilenameOfPath(self, path):
        """
        Returns the last two segments of a file path
        """
        return os.path.join(
            os.path.basename(os.path.dirname(path)),
            os.path.basename(path))

    def testCompile(self):
        """
        Compiles the schemas to a temporary directory and then checks
        that the pb2 files in the temporary direcory are the same as the
        pb2 files that are checked in.

        This test prevents inadvertent mismatches between proto files and
        pb2 files from being checked in.
        """
        # compile the schemas to a temporary directory
        scriptPath = 'scripts/process_schemas.py'
        schemaVersion = '.'.join(version.version.split('.')[0:3])
        schemasDir = 'src/main/proto/'
        schemaDest = tempfile.mkdtemp()
        cmd = "python {} {} -s {} -d {}".format(
            scriptPath, schemaVersion, schemasDir, schemaDest)
        utils.runCommand(cmd, silent=True)

        # get the file paths of the checked in pb2 files
        # (we do it in two calls to avoid the build/ tree, etc.
        # in the python directory which may contain pb2 files)
        pb2Patterns = ["*_pb2.py"]
        checkedInDirGa4gh = 'python/candig/schemas/candig/'
        checkedInDirGoogle = 'python/candig/schemas/google/'
        checkedInFilePathsGa4gh = utils.getFilePathsWithExtensionsInDirectory(
                checkedInDirGa4gh, pb2Patterns)
        checkedInFilePathsGoogle = utils.getFilePathsWithExtensionsInDirectory(
                checkedInDirGoogle, pb2Patterns)
        checkedInFilePaths = sorted(
            checkedInFilePathsGa4gh + checkedInFilePathsGoogle)

        # check to see that the contents of the directories are the same
        tempFilePaths = utils.getFilePathsWithExtensionsInDirectory(
            schemaDest, pb2Patterns)
        self.assertEqual(len(checkedInFilePaths), len(tempFilePaths))
        for checkedInFilePath, tempFilePath in utils.zipLists(
                checkedInFilePaths, tempFilePaths):
            checkedInFileShortPath = self._getDirAndFilenameOfPath(
                checkedInFilePath)
            tempFileShortPath = self._getDirAndFilenameOfPath(tempFilePath)
            self.assertEqual(checkedInFileShortPath, tempFileShortPath)
            utils.assertFileContentsIdentical(
                checkedInFilePath, tempFilePath)
