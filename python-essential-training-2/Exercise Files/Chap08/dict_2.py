#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def main():
    animals2 = dict(kitten='meow', puppy='ruff!', lion='grrr',
                    giraffe='I am a giraffe!', dragon='rawr')
    animals = {'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
               'giraffe': 'I am a giraffe!', 'dragon': 'rawr'}
#
    # for k in animals.keys():
    #     print(f'{k}')

    # for v in animals.values():
    #     print(f'{v}')

    # print_dict(animals2)
    animals['lion'] = 'I am a lion'
    print(animals['lion'])
    animals['monkey'] = 'haha'
    print_dict(animals)
    print('Found!' if 'lion' in animals else 'Nope!')
    # print(animals['dog'])

    print(animals.get('dog'))

def print_dict(o):
    for x in o:
        print(f'{x}: {o[x]}')


if __name__ == '__main__':
    main()
