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

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.
def first(s):
    return s[0]
def utility(filename):
    user_file = open(filename, 'rU')
   # string = f.read()
   # list_of_words = (string.lower()).split()
    #list_of_words = sorted(list_of_words, key=first)
    #print list_of_words
    diction = {}
    for line in user_file:
        words = line.split()
        for word in words:
            word = word.lower()
            if not word in diction:
                diction[word] = 1
            else:
                diction[word] += 1
        #count = 2
        #copyOf = word
        #while copyOf in list_of_words:
            #list_of_words.remove(copyOf)
            #count += 1
        #dict[copyOf] = count
    user_file.close()
    return diction

def print_words(filename):
    dictionary = utility(filename)
    for keys in sorted(dictionary.keys()):
        print '%-15s %2s %4d\n'% (keys,'=',dictionary[keys])

def word_count(val):
    return val[1]

def print_top(filename):
    dictnry = utility(filename)
    tuples = sorted(dictnry.items(), key=word_count, reverse=True)
    for i in tuples[:20]:
        print '%-15s %2s %4d'% (i[0],'=', i[1])
    #val_list = list(dictnry.values())
    #val_list = sorted(val_list)
    #val_list.reverse()
    #top20 = 20
    #for val in val_list:
        #for k, v in dictnry.items():
            #if val == v:
                #print '%-15s %2s %4d\n'% (k,'=', val)
                #del dictnry[k]
                #top20 -= 1
                #break
        #if top20 == 0:
            #break


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
