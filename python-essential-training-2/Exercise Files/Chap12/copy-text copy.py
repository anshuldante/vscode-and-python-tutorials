#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('/Users/a0a00uj/python/python-practice-2/Ex_Files_Python_EssT/Exercise Files/Chap12/lines.txt', 'rt')
    outfile = open('/Users/a0a00uj/python/python-practice-2/Ex_Files_Python_EssT/Exercise Files/Chap12/lines-copy.txt', 'wt')
    outfile2 = open('/Users/a0a00uj/python/python-practice-2/Ex_Files_Python_EssT/Exercise Files/Chap12/lines-copy2.txt', 'wt')
    outfile3 = open('/Users/a0a00uj/python/python-practice-2/Ex_Files_Python_EssT/Exercise Files/Chap12/lines-copy3.txt', 'wt')
    outfile4 = open('/Users/a0a00uj/python/python-practice-2/Ex_Files_Python_EssT/Exercise Files/Chap12/lines-copy4.txt', 'wt')
    for line in infile:
        outfile.writelines(line)
        outfile2.writelines(line.rstrip())
        print(line.rstrip(), file=outfile3)
        print(line, file=outfile4)
        print('.', end='', flush=True)

        # print uses OS default new lines, weitelines doesn't
    outfile.close()
    infile.close()
    print('\ndone.')

if __name__ == '__main__': main()
