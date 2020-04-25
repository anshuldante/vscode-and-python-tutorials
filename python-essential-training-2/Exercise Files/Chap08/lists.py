#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    game2 = ( 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' )
    print_list(game)
    print_list(game2)
    print(', '.join(game))
    print(len(game))
    print(game[1:5:2])
    print(game.index('Paper'))
    game.append('Computer')
    game.insert(0,'Mouse')
    game.remove('Paper')
    print(game.pop())
    print(game.pop(2))
    del game[1]
    del game[1:2:1]
    print_list(game)

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()
