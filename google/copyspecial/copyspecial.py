#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import os
import re
import shutil
import commands

"""Copy Special exercise
"""

def getSpecialFilePaths(dir):
    """Gets all of the special files in the directory. Each file returned is the absolute file path."""
    # Get the names of the files in the directory
    fileNames = os.listdir(dir)

    # Check if they are a special file and if so convert them into their absolute paths
    paths = []
    for filename in fileNames:
        if re.search(r"__\w+__", filename):
            paths.append(os.path.abspath(os.path.join(dir, filename)))

    return paths


def copyFiles(files, dir):
    """Copy all of the files to the specified directory."""
    # Make sure the directory exists first
    if not os.path.exists(dir):
        os.makedirs(dir)

    # Copy the files across
    for file in files:
        filename = os.path.basename(file)
        shutil.copy(file, os.path.join(dir, filename))


def zipFiles(files, zipFile):
    """Pack the files into a ZIP archive using the name provided"""
    command = "zip -j " + zipFile
    for file in files:
        command += " " + file

    # print what command is going to be run
    print "Command I'm going to do:", command

    # run the command
    (exitStatus, output) = commands.getstatusoutput(command)

    # if an error occurred print the output to stderr and exit
    if exitStatus:
        print >>sys.stderr, output
        sys.exit(1)


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print "usage: [--todir dir][--tozip zipfile] dir [dir ...]"
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print "error: must specify one or more dirs"
        sys.exit(1)

    # Get all the file names/paths
    specialFiles = []
    for dir in args:
        specialFiles.extend(getSpecialFilePaths(dir))

    # Print/copy/zip the files based on the arguments
    if todir != "":
        copyFiles(specialFiles, todir)
    elif tozip != "":
        zipFiles(specialFiles, tozip)
    else:
        print "\n".join(specialFiles)


if __name__ == "__main__":
    main()
