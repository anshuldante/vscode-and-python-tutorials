#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from decimal import *

a = Decimal('0.10')
b = Decimal('0.30')

y = 3 * a - b

print('x is {}'.format(y))
print(type(y))


x = .1+.1+.1-.3
print('x is {}'.format(x))
print(type(x))
