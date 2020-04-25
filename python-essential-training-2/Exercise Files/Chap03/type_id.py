#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = (1, 'two', 3.0, [4, 'four'], 5)
y = [1, 'two', 3.0, [4, 'four'], 5]
print('x is {}'.format(x))
print(type(x))
print(type(y))

print(id(x))
print(id(y))

print(id(x[0]))
print(id(y[0]))

if x[0] is y[0]:
    print("Yep")
else:
    print("Nope")

if x is y:
    print("Yep")
else:
    print("Nope")

if isinstance(y,tuple):
    print("tuple")
elif isinstance(y, list):
    print('list')
else:
    print("Nope")