#!/usr/bin/env python
# coding: utf-8

import fnmatch
import os

def locate(pattern, root=os.curdir):
    '''Locate all files matching supplied filename pattern in and below
    supplied root directory.'''
        #ignore directories- uncomment to make ignore work
    #ignored = ["0201", "0306"]
    for path, dirs, files in os.walk(os.path.abspath(root)):
        #for dir in ignored:
           # if dir in dirs:
                #dirs.remove(dir)
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(path, filename)

if __name__ == '__main__':
    for filename in locate('*.sss'):
        print(filename)
