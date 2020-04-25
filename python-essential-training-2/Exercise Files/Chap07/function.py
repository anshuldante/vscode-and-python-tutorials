#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def main():
    print('Main.')
    x = 5
    y = 5
    print(id(x))
    print(id(y))
    x = [5]
    y = x
    y[0] = 3
    print(id(x))
    print(id(y))
    print(x)
    print(y)
    kitten2(x, 6)
    print(f'in main: x is {x}')


def kitten(a, b=1, c=0):
    print('Meow.')

    print(a, b, c)


def kitten2(a, b=1, c=0):
    a[0] = 3
    print(id(a))
    a = 3
    print(id(a))
    print(a, b, c)


if __name__ == '__main__':
    main()
