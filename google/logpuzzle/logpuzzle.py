#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def secondWordSorter(a):
    """A specialised sorter, to sort on the second word in a '-<WORD>-<WORD>.<FILE_EXT>' string."""
    match = re.search(r"-\w+-(\w+)\.\w+", a)
    if match:
        return match.group(1)
    else:
        return a


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""

    # Calculate the host
    host = "http://" + filename.split("_", 1)[1]

    # Open the file
    f = open(filename, "rU")

    # Find the puzzle urls
    # Note: I'm using a set to remove duplicates
    puzzleUrls = set()
    for line in f:
        match = re.search(r"GET\s+(\S*puzzle\S*)\s+HTTP", line)
        if match:
            puzzleUrls.add(host + match.group(1))

    # Close the file
    f.close()

    # Sort the urls and return the list
    return sorted(puzzleUrls, key=secondWordSorter)


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    # Make sure the directory exists first
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Make the base of the index page
    index = "<html>\n\t<body>\n\t\t"

    # Download each image into the directory
    for i, imgUrl in enumerate(img_urls):
        filename = "img%d" % i
        print "Retrieving...", imgUrl
        urllib.urlretrieve(imgUrl, os.path.join(dest_dir, filename))
        index += "<img src=\"%s\"/>" % filename

    # Finish up the index page and save it
    index += "\n\t</body>\n</html>"
    f = open(os.path.join(dest_dir, "index.html"), "w")
    f.write(index)
    f.close()


def main():
    args = sys.argv[1:]

    if not args:
        print 'usage: [--todir dir] logfile '
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print '\n'.join(img_urls)


if __name__ == '__main__':
    main()
