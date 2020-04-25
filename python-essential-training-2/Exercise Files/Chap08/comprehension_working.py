#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from math import pi


def main():
    seq = range(11)
    seq2 = [x*2 for x in seq]
    seq2 = [x for x in seq if x % 3 != 0]
    seq2 = [(x, x**2) for x in seq]
    seq2 = [round(pi, x) for x in seq]
    seq3 = {x: x**2 for x in seq}
    seq3 = {x for x in 'superduper' if x not in 'pd'}
    print(seq3)
    print_list(seq)
    print_list(seq2)


def print_list(o):
    for x in o:
        print(x, end=' ')
    print()


if __name__ == '__main__':
    main()
