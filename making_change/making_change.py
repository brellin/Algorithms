#!/usr/bin/python

import sys


def making_change(amount, denominations):
    cache = [0 for a in range(amount + 1)]
    cache[0] = 1

    for d in denominations:
        n = d
        while n <= amount:
            cache[n] += cache[n - d]
            print(cache)
            n += 1

    return max(cache)


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
