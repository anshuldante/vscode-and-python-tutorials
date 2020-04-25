#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class bunny:
    def __init__(self, n):
        self._n=n
    def __repr__(self):
        return f'repr: the number of bunnies is {self._n} 🖖'
    def __str__(self):
        return f'str: the number of bunnies is {self._n}'

s='Hello, World.'
print(repr(s))


s2=bunny(45)
print(repr(s2))
print(ascii(s2))
print(str(s2))
print(chr(128406))
print(ord('🖖'))
print(s2)