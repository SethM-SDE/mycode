#!/usr/bin/env python3

def starbuilder(starcount):
    for star in starcount:
        counter = 0
        while counter < star:
            print('*', end="")
            counter += 1
        print('')

def starbuilder2(starcount):
    for star in starcount:
        print('*' * star)

def main():
    starbuilder(range(1,5))
    starbuilder(range(5,0, -1))
    starbuilder2(range(1,5))
    starbuilder2(range(5,0,-1))

main()
