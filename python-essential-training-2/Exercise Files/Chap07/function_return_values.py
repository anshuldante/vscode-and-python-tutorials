#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def main():
    x = kitten()
    print(x)
    print(type(x))


def kitten():
    print('Meow.')
    #return 5
    #return [1, 2, 3]
    #return (1, 2, 3, 4)
    return dict(Two=2, Four=4)


if __name__ == '__main__':
    main()
