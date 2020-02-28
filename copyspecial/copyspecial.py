#!/usr/bin/python2
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import subprocess
"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def absolute_paths(source_dir):
    if not  os.path.exists(source_dir):
        print ('error: Path does not exist')
        sys.exit(1)
    filenames = os.listdir(source_dir)
    list_paths = []
    for filename in filenames:
        match = re.search(r'[\w.-]+__[\w.-]+__[\w.-]+',filename)
        if match:
            list_paths.append(os.path.abspath(os.path.join(source_dir,filename)))
    return list_paths

def copy_files(t_dir, s_paths):
    if not  os.path.exists(t_dir):
        os.mkdir(t_dir)
    for path in s_paths:
        shutil.copy(path, t_dir)

def zip_files(filename, s_paths):
    cmd = 'zip -j ' + filename + ' ' + ' '.join(s_paths)
    p_out = subprocess.Popen(cmd, shell=True,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print (p_out.stdout.readlines())
    return



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print ("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
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
    print ("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  paths= []
  paths = absolute_paths(args[len(args) -1])
  if todir:
      copy_files(todir, paths)
  elif tozip:
      zip_files(tozip, paths)
  else:
      paths = absolute_paths(args[0])
      for path in paths:
          print (path)



if __name__ == "__main__":
  main()
