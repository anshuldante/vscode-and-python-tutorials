#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.')

print('Hello, World.'.upper())
print('Hello, World.'.lower())
print('Hello, World.'.capitalize())

print('Hello, World.'.title())
print('Hello, World. ß'.casefold())
print('Hello, World. ß'.lower())

s1 = 'Hello, World.'
s2 = 'Hello, World.'.upper()

print(id(s1))
print(id(s2))

s3 = 'I am a string'
s4 = 'I am another one'

s5 = 'this str' + ' ' + 'that str'

print(s3 + ' ' + s4)
print(s5)
