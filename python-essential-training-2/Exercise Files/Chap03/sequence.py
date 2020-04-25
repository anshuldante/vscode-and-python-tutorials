#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Ranges are immutable and only work for numbers
x = range(5, 50, 5)

for i in x:
    print('i is {}'.format(i))

print(type(x))
print('-----------------')

# Tuples are immutable
x = (1, 2, 3, 4, 5)

for i in x:
    print('i is {}'.format(i))

print(type(x))
print('-----------------')
# Lists are mutable
x = [1, 2, 3, 4, 5]

x = list(range(5, 50, 5))

x[4] = 42

for i in x:
    print('i is {}'.format(i))

print(type(x))
print('-----------------')
# Dictionaries is a seachable sequence of key-value pairs and are immutable
x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

x['three'] = 42

for k, v in x.items():
    print('k: {}, v: {}'.format(k, v))

print(type(x))
print('-----------------')
