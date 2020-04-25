#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# and or not in not in is is not

a = True
b = False
x = ( 'bear', 'bunny', 'tree', 'sky', 'rain' )
y = 'bear'

if not a:
    print('expression is true')
else:
    print('expression is false')

if y is x[0]:
    print('expression is true')
else:
    print('expression is false')

print(id(y))
print(id(x[0]))