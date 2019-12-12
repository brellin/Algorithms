#!/usr/bin/python

import sys

rps = [
    ['rock'],
    ['paper'],
    ['scissors']
]


def rock_paper_scissors(n):

    possibilities = []

    def add_possiblility(n, arr):

        if n == 0:
            return possibilities.append(arr)

        for possibility in rps:
            add_possiblility(n - 1, arr + possibility)

    add_possiblility(n, [])

    return possibilities


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
