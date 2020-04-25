#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = '47'
y = int(x)
z = float(x)*-1
a = divmod(y, 3)
b = y + 2j
c = complex(y , 21)

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')
print(f'z is {type(z)}')
print(f'z abs is {abs(z)}')
print(f'z is {z}')
print(f'a is {a}')
print(f'b is {b}')
print(f'b is {type(b)}')
print(f'c is {c}')
print(f'c is {type(c)}')