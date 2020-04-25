#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

y = 'seven "{1:<09}" "{0:>09}"'.format(8, 1234)
a=8
b=9
x = f'seven {a:<09} {b:>09} {12}'
print('x is {}'.format(x))
print(type(x))
