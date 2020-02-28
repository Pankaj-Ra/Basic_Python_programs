#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import subprocess

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  names_dict = {}
  names_file = open(filename, 'rU')
  names_string= names_file.read()
  names_file.close()
  match = re.search('(Popularity in)\s(\d\d\d\d)', names_string)
  if match:
      names_dict[match.group(2)] = ''
  tuples = re.findall(r'(\d+)</td><td>(\w+)</td><td>(\w+)', names_string)
  for items in tuples:
      (rank, boyname, girlname) = items  # unpack the tuple into 3 vars
      names_dict[boyname] = rank
      names_dict[girlname] = rank
  return names_dict

def print_babynames(filename):
    baby_dict = extract_names(filename)
    for k , v in sorted(baby_dict.items()):
        print '%-10s %4s'% (k, v)
    return

def summary_catalog(filename):
    names_dict = extract_names(filename)
    out_file = open(filename + '.summary', 'w')
    #sys.stdout = out_file
    for k, v in sorted(names_dict.items()):
        print >> out_file, '%-10s %4s'% (k, v)
        #print('%-10s %4s'% (k,v), file=out_file)
    #sys_stdout = orig_stdout
    out_file.close()
    return
def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
      print 'usage: [--summaryfile] file [file ...]'
      sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
      summary = True
      del args[0]

  # +++your code here+++
  if summary:
      # Set up find command
     #findCMD = 'find '+ args[0]
     #print findCMD
     #out = subprocess.Popen(findCMD,shell=True,stdin=subprocess.PIPE,
     #                                stdout=subprocess.PIPE,stderr=subprocess.PIPE)
     ## Get standard out and error
     #(stdout, stderr) = out.communicate()
     ## Save found files to list
     #filelist = stdout.decode().split()
     for filename in args:
         summary_catalog(filename)
  else:
      print_babynames(args[0])
  # For each filename, get the names, then either print the text output
  # or write it to a summary file

if __name__ == '__main__':
    main()
