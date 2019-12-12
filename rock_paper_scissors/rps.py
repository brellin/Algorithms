#!/usr/bin/python

import sys

rps = [
    ['rock'],
    ['paper'],
    ['scissors']
]

possibilities = []


def add_possiblility(n, arr):

    print(f'possibility: {n}')

    if n == 0:
        return possibilities.append(arr)

    for possibility in rps:
        add_possiblility(n - 1, arr + possibility)


def rock_paper_scissors(n):
    add_possiblility(n, [])

    return possibilities


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
