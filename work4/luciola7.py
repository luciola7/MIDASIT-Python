#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def extract_second_word(fullpath):
    words = fullpath.split('-')

    for word in words:
        if word.find('.jpg') > -1:
            return word

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  
  urls = set()
  rex_path = re.compile('.+\s\"GET\s(\S+puzzle\S+)')
  #rex_path = re.compile('.+\s\"GET\s(\S)\s')
  f = open(filename, 'r')
  while True:
    line = f.readline()
    if not line: break
    rst = rex_path.search(line);
    if rst:
      urls.add(rst.group(1))
  # Sort urls
  return sorted(urls, key=extract_second_word)
  
def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  domain_url = 'http://code.google.com'
  img_prefix = 'img'
  img_extention = '.jpg'
  img_files = list()
  for idx, img_url in enumerate(img_urls):
    print(img_url)
    # if idx > 10: break
    local_filename, headers = urllib.request.urlretrieve(domain_url + img_url)
    img_file = dest_dir + img_prefix + str(idx) + img_extention;
    os.rename(local_filename, img_file)
    img_files.append(img_file)
    
  with open(dest_dir+'/index.html', mode='w', encoding='utf-8') as f:
        f.write('<vervatim>\n<html>\n<body>\n')
        for img in img_files:
            f.write('<img src="' + img + '">')
        f.write('\n<body>\n<html>')

def main():
  py_path = os.path.dirname(os.path.abspath(__file__))

  # input_file = py_path + '\\animal_code.google.com'
  input_file = py_path + '\\place_code.google.com'
  args = sys.argv[1:]

  if not args:
    todir = './'
  else:
    if args[0] == '--todir':
      todir = args[1]
      del args[0:2]
    input_file = args[0]
    
  img_urls = read_urls(input_file)

  if todir:
    download_images(img_urls, todir)
  else:
    print('\n'.join(img_urls))

if __name__ == '__main__':
  main()
