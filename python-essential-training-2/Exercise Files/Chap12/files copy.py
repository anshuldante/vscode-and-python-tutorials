#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


import os


def main():
    print(os.listdir('/Users/a0a00uj/python/python-practice-2/Ex_Files_Python_EssT/Exercise Files/Chap12/'))

    f = open('/Users/a0a00uj/python/python-practice-2/Ex_Files_Python_EssT/Exercise Files/Chap12/lines.txt', 'r+t')
    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()
