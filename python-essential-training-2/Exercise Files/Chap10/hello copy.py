#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys

def main():
    try:
        x = int('1')
        y = 5/2
        z = 1 - '123'
    except ValueError:
        print('I cought a ValueError')
    except ZeroDivisionError:
        print("Don't divide by zero")
    except:
        print(f'Unknown error: {sys.exc_info()}')
    else:
        print('Good job!')
        print(x, y)

if __name__ == '__main__': main()
