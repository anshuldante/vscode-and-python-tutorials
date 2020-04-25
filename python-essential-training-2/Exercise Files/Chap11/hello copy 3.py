#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


x = 42
y=73

print('the number us {bb} {xx}'.format(xx = x, bb= y))


print('the number us {1} {0} {0}'.format(x, y))

print('the number us {0:<05} {1:>05} ..'.format(x, y))


print('the number us {0:<05} {1:+05} ..'.format(x, y))


x = 42*74712311123123123
print('the number is {}'.format(x))
print('the number is {:,}'.format(x).replace(',','.'))
print('the number is {:.7f}'.format(x))


x=42

print('the number is {:x}'.format(x))
print('the number is {:o}'.format(x))
print('the number is {:b}'.format(x))

print(f'the number is {x:.3f}')