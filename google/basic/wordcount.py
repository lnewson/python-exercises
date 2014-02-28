#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.


def last(a):
    """Get the last element in a list"""
    return a[-1]


def print_words(filename):
    """Print the all words in a file sorted alphabetically, along with the number of times each word is used."""
    sortedDict = sorted(buildWordDictionary(filename).items())

    for word in sortedDict:
        print word[0], word[1]


def print_top(filename):
    """Print the top 20 most used words from a file, with the number of times each word is used."""
    dict = sorted(buildWordDictionary(filename).items(), key=last, reverse=True)

    for word in dict[:20]:
        print word[0], word[1]


def readFileContents(filename):
    """Read in the full contents of a file."""
    f = open(filename, "rU")
    content = f.read()
    f.close()
    return content


def buildWordDictionary(filename):
    """Build the word count dictionary from the words in the specified file."""
    content = readFileContents(filename)
    words = content.split()
    dict = {}
    for word in words:
        lowerWord = word.lower()
        if lowerWord in dict:
            dict[lowerWord] += 1
        else:
            dict[lowerWord] = 1
    return dict


###
# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print 'usage: ./wordcount.py {--count | --topcount} file'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print 'unknown option: ' + option
        sys.exit(1)


if __name__ == '__main__':
    main()
