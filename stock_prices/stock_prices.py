#!/usr/bin/python

import argparse


def find_max_profit(prices):
    max_profit = prices[len(prices) - 1] - prices[0]

    # loop over all but last item
    for i in range(len(prices) - 2):
        # loop over each item after current item (including last item)
        for j in range(i + 1, len(prices) - 1):
            # if ((any item after current item) - current item) > profit, replace profit
            new_profit = prices[j] - prices[i]
            max_profit = new_profit if new_profit > max_profit else max_profit

    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
