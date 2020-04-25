#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('/Users/a0a00uj/python/python-practice-2/Ex_Files_Python_EssT/Exercise Files/Chap12/berlin.jpg', 'rb')
    outfile = open('/Users/a0a00uj/python/python-practice-2/Ex_Files_Python_EssT/Exercise Files/Chap12/berlin-copy.jpg', 'wb')
    while True:
        buf = infile.read(10240)
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
