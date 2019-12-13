#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache={}):
    # base cases
    if n == 0:
        return 1
    elif n < 3:
        return n
    elif n == 3:
        return 4

    # repeat until base cases are met
    elif n not in cache:
        cache[n] = eating_cookies(
            n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

    # return when base cases are returned up the recursive line
    return cache[n]


# 5

# 1 1 1 1 1
# 1 2 1 1
# 1 1 2 1
# 1 1 1 2
# 1 2 1
# 1 1 2
# 1 3 1
# 1 1 3
# 2 1 1 1
# 2 2 1
# 2 3
# 3 1 1
# 3 2

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
