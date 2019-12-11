#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):

    track = {}

    for k, v in ingredients.items():
        track[k] = 0
        while v >= recipe[k]:
            track[k] += 1
            v -= recipe[k]

    return min(track.values()) if len(ingredients) == len(recipe) else 0


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
