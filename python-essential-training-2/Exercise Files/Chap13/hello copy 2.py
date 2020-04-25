#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = (1, 2, 3, 4, 5)
y = (6, 7, 8, 9, 10)
a = x
b = len(x)
c = reversed(x)
d = list(reversed(x))
e = sum(x)
f = sum(x, 10)
g = max(x)
h = min(x)
i = any(x)
j = any((0, 0, 0, 0))
j = all(x)
k = zip(x, y)
print(x)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
for a,b in k : print(f'{a}, {b}')


x = ('bear', 'monkey', 'mouse')

for i, v in enumerate(x): print(f'{i}: {v}')