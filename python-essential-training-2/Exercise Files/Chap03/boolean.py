#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = False
print('x is {}'.format(x))
print(type(x))


y = None # None, Numeric 0s and Empty string always return false

if y:
    print("True")
else:
    print('False')