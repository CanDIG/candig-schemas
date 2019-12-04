"""
A script to generate the schemas for the GA4GH protocol. These are generated
from a copy of the Protocol Buffers schema and use it to generate
the Python class definitions. These are also stored in revision
control to aid Travis building.
"""

import os
import os.path
import subprocess
import fnmatch
import re
import argparse
import shlex
import glob


# IMPORTANT!
# Do not import any candig or otherwise non-standard packages in this file.
# process_schemas is included in candig-schema's install path in setup.py.
# Importing, for instance, candig-common here will break an install if
# the environment does not have that package installed previously.
# We really want to avoid this scenario!
# (This does result in some code duplication in this file.)

# Below code duplicated from candig-common

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


def runCommand(command, silent=False, shell=False):
    """
    Run a shell command
    """
    splits = shlex.split(command)
    runCommandSplits(splits, silent=silent, shell=shell)

# Above code duplicated from ga4gh-common


class ProtobufGenerator(object):

    def __init__(self, version):
        self.version = version

    def _createSchemaFiles(self, destPath, schemasPath):
        """
        Create a hierarchy of proto files in a destination directory, copied
        from the schemasPath hierarchy
        """
        # Create the target directory hierarchy, if neccessary
        ga4ghPath = os.path.join(destPath, 'candig')
        if not os.path.exists(ga4ghPath):
            os.mkdir(ga4ghPath)
        ga4ghSchemasPath = os.path.join(ga4ghPath, 'schemas')
        if not os.path.exists(ga4ghSchemasPath):
            os.mkdir(ga4ghSchemasPath)
        ga4ghSchemasGa4ghPath = os.path.join(ga4ghSchemasPath, 'candig')
        if not os.path.exists(ga4ghSchemasGa4ghPath):
            os.mkdir(ga4ghSchemasGa4ghPath)
        ga4ghSchemasGooglePath = os.path.join(ga4ghSchemasPath, 'google')
        if not os.path.exists(ga4ghSchemasGooglePath):
            os.mkdir(ga4ghSchemasGooglePath)
        ga4ghSchemasGoogleApiPath = os.path.join(
            ga4ghSchemasGooglePath, 'api')
        if not os.path.exists(ga4ghSchemasGoogleApiPath):
            os.mkdir(ga4ghSchemasGoogleApiPath)

        # rewrite the proto files to the destination
        for root, dirs, files in os.walk(schemasPath):
            for protoFilePath in fnmatch.filter(files, '*.proto'):
                src = os.path.join(root, protoFilePath)
                dst = os.path.join(
                    ga4ghSchemasPath,
                    os.path.relpath(root, schemasPath), protoFilePath)
                self._copySchemaFile(src, dst)

    def _doLineReplacements(self, line):
        """
        Given a line of a proto file, replace the line with one that is
        appropriate for the hierarchy that we want to compile
        """
        # candig packages
        packageString = 'package candig;'
        if packageString in line:
            return line.replace(
                packageString,
                'package candig.schemas.candig;')
        importString = 'import "candig/'
        if importString in line:
            return line.replace(
                importString,
                'import "candig/schemas/candig/')
        # google packages
        googlePackageString = 'package google.api;'
        if googlePackageString in line:
            return line.replace(
                googlePackageString,
                'package candig.schemas.google.api;')
        googleImportString = 'import "google/api/'
        if googleImportString in line:
            return line.replace(
                googleImportString,
                'import "candig/schemas/google/api/')
        optionString = 'option (google.api.http)'
        if optionString in line:
            return line.replace(
                optionString,
                'option (.candig.schemas.google.api.http)')
        return line

    def _copySchemaFile(self, src, dst):
        """
        Copy a proto file to the temporary directory, with appropriate
        line replacements
        """
        with open(src) as srcFile, open(dst, 'w') as dstFile:
            srcLines = srcFile.readlines()
            for srcLine in srcLines:
                toWrite = self._doLineReplacements(srcLine)
                dstFile.write(toWrite)

    def _find_in_path(self, cmd):
        PATH = os.environ.get("PATH", os.defpath).split(os.pathsep)
        for x in PATH:
            possible = os.path.join(x, cmd)
            if os.path.exists(possible):
                return possible
        return None

    def _assertSchemasExist(self, schemas_path):
        if not os.path.exists(schemas_path):
            raise Exception(
                "Can't find schemas folder. " +
                "Thought it would be at {}".format(
                    os.path.realpath(schemas_path)))

    def _assertProtoDirectoryExists(self, source_path):
        if not os.path.exists(source_path):
            msg = "Can't find source proto directory {}".format(
                os.path.realpath(source_path))
            raise Exception(msg)

    # https://stackoverflow.com/questions/22490366/how-to-use-cmp-in-python-3
    def _cmp(self, a, b):
        return (a > b) - (a < b)

    # From http://stackoverflow.com/a/1714190/320546
    def _version_compare(self, version1, version2):
        def normalize(v):
            return [int(x) for x in re.sub(r'(\.0+)*$', '', v).split(".")]
        return self._cmp(normalize(version1), normalize(version2))

    def _getProtoc(self, destination_path):
        protocs = [os.path.realpath(x) for x in
                   ("{}/protobuf/src/protoc".format(destination_path),
                   self._find_in_path("protoc"))
                   if x is not None]
        protoc = None
        for c in protocs:
            if not os.path.exists(c):
                continue
            output = subprocess.check_output([c, "--version"]).strip()
            try:
                (lib, version) = output.decode('utf-8').split(" ")
                if lib != "libprotoc":
                    raise Exception("lib didn't match 'libprotoc'")
                if self._version_compare("3.0.0", version) > 0:
                    raise Exception("version < 3.0.0")
                protoc = c
                break
            except Exception:
                print(
                    "Not using {path} because it returned " +
                    "'{version}' rather than \"libprotoc <version>\", where " +
                    "<version> >= 3.0.0").format(path=c, format=output)

        if protoc is None:
            raise Exception("Can't find a good protoc. Tried {}".format(
                protocs))
        print("Using protoc: '{}'".format(protoc))
        return protoc

    def _writePythonFiles(self, source_path, protoc, destination_path):
        protos = []
        for root, dirs, files in os.walk(source_path):
            protos.extend([
                os.path.join(root, f)
                for f in fnmatch.filter(files, "*.proto")])
        if len(protos) == 0:
            raise Exception(
                "Didn't find any proto files in '{}'".format(source_path))
        print("pb2 files destination: '{}'".format(destination_path))
        cmdString = (
            "{protoc} -I {source_path} -I ./src/main "
            "--python_out={destination_path} {proto_files}")
        cmd = cmdString.format(
            protoc=protoc, source_path=source_path,
            destination_path=destination_path,
            proto_files=" ".join(protos))
        runCommand(cmd)
        print("{} pb2 files written".format(len(protos)))

    def _writeVersionFile(self):
        versionFilePath = "python/candig/schemas/_protocol_version.py"
        try:
            with open(versionFilePath, "w") as version_file:
                self._writeVersion(version_file)
        except FileNotFoundError:
            # Write version when running from /scripts
            with open("../" + versionFilePath, "w") as version_file:
                self._writeVersion(version_file)

    def _writeVersion(self, version_file):
        version_file.write(
            "# File generated by scripts/process_schemas.py; "
            "do not edit\n")
        version_file.write("version = '{}'\n".format(self.version))

    def _deleteProtoFilesInDestinationPath(self, destination_path):

        filelist = glob.glob(os.path.join(
            destination_path, "candig/schemas/candig/*.proto"))

        for f in filelist:
            os.remove(f)

        print("Temporary proto files all deleted")

    def run(self, args):
        script_path = os.path.dirname(os.path.realpath(__file__))
        destination_path = os.path.realpath(
            os.path.join(script_path, args.destpath))
        schemas_path = os.path.realpath(args.schemapath)
        protoc = self._getProtoc(destination_path)
        print("Writing protocol version '{}'".format(args.version))
        print("Proto files source: '{}'".format(schemas_path))
        print("Rewritten proto files source: '{}'".format(destination_path))
        self._createSchemaFiles(destination_path, schemas_path)
        self._writePythonFiles(destination_path, protoc, destination_path)
        self._deleteProtoFilesInDestinationPath(destination_path)
        self._writeVersionFile()


def main(args=None):
    defaultDestPath = "../python/"
    defaultSchemasPath = '../src/main/proto/'
    parser = argparse.ArgumentParser(
        description="Script to process GA4GH Protocol buffer schemas")
    parser.add_argument(
        "version", help="Version number of the schema we're compiling")
    parser.add_argument(
        "-s", "--schemapath", default=defaultSchemasPath,
        help="Path to schemas (defaults to {})".format(defaultSchemasPath))
    parser.add_argument(
        "-d", "--destpath", default=defaultDestPath,
        help=(
            "the directory in which to write the compiled schema files "
            "(defaults to {})".format(defaultDestPath)))
    parsedArgs = parser.parse_args(args)
    pb = ProtobufGenerator(parsedArgs.version)
    pb.run(parsedArgs)


if __name__ == "__main__":
    main()
