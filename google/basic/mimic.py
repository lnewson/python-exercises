#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import sys
import random


def readFileContents(filename):
    """Read in the full contents of a file."""
    f = open(filename, "rU")
    content = f.read()
    f.close()
    return content


def mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""
    fileContents = readFileContents(filename)
    splitWords = fileContents.split()

    # Build up the mimic dictionary
    mimicDict = {}
    lastWord = ""
    for word in splitWords:
        if lastWord in mimicDict:
            mimicDict[lastWord].append(word)
        else:
            mimicDict[lastWord] = [word]
        lastWord = word

    return mimicDict


def print_mimic(mimic_dict, word):
    """Given mimic dict and start word, prints 200 random words."""
    # Die when the word isn't in the mimic dictionary
    if word not in mimic_dict:
        return

    # Start printing the words
    _print_mimic(mimic_dict, word, 0, 0)


def _print_mimic(mimic_dict, word, wordCount, lineCharCount):
    """Given mimic dict and start word, prints 200 random words."""
    # Check if we've reached 200 words yet
    if wordCount >= 200:
        return

    # Get the random word to print
    wordList = mimic_dict[word]
    randomWord = random.choice(wordList)
    lineCharCount = print_word(randomWord, lineCharCount)

    # Check that the random word exists in the dictionary, if not start back at the empty string
    if randomWord in mimic_dict:
        _print_mimic(mimic_dict, randomWord, wordCount + 1, lineCharCount)
    else:
        _print_mimic(mimic_dict, "", wordCount + 1, lineCharCount)


def print_word(word, lineCharCount):
    """Prints a word so that the output is formatted to a maximum column width of 70 characters."""
    if len(word) + lineCharCount > 70:
        print "\n" + word,
        return len(word) + 1
    else:
        print word,
        return len(word) + 1 + lineCharCount


# Provided main(), calls mimic_dict() and mimic()
def main():
    if len(sys.argv) != 2:
        print 'usage: ./mimic.py file-to-read'
        sys.exit(1)

    mimicDict = mimic_dict(sys.argv[1])
    print_mimic(mimicDict, '')


if __name__ == '__main__':
    main()
