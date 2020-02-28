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
import subprocess

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def url_sort_key(url):
  """Used to order the urls in increasing order by 2nd word if present."""
  match = re.search(r'-(\w+)-(\w+)\.\w+', url)
  if match:
    return match.group(2)
  else:
    return url


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  url_match = re.search(r'_[\w.]+com',filename)
  urlname = 'http://' + ''.join(url_match.group()[1:])
  files = open(filename, 'rU')
  random_urls = files.read()
  url_results = re.findall(r'[\w/-]+/puzzle/[\w.-]+jpg',random_urls)
  url_list =[]
  for addres in url_results:
      url = urlname + addres
      if not url in url_list:
          url_list.append(url)
  files.close()
  return sorted(url_list, key=url_sort_key)

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  if not os.path.exists(dest_dir):
      os.mkdir(dest_dir)
  index = file(os.path.join(dest_dir, 'index.html'), 'w')
  index.write('<html><body>\n')
  count = 0
  for url in img_urls:
      img_name = 'img' + str(count) + '.jpg'
      print 'Retreiving...  ' + url
      urllib.urlretrieve(url, os.path.join(dest_dir, img_name))
      count += 1
      index.write('<img src="%s">' % (img_name,))
      #cmd = 'mv ' + img_name + ' ' + dest_dir
      #p_out = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  index.write('\n</body></html>\n')
  index.close()
  return

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
