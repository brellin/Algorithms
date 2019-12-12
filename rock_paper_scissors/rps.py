#!/usr/bin/python

import sys

rps = [
    ['rock'],
    ['paper'],
    ['scissors']
]


def add_possibility(n, curr, acc):

    if n == 0:
        return acc.append(curr)

    possibility = 0
    while possibility < 3:
        add_possibility(n - 1, curr + rps[possibility], acc)
        possibility += 1


def rock_paper_scissors(n):

    possibilities = []

    add_possibility(n, [], possibilities)

    return possibilities


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
