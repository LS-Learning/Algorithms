#!/usr/bin/python

import math

recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }

def recipe_batches(recipe, ingredients):
    if len(recipe.keys()) != len(ingredients.keys()):
        return 0
    else:
        dict = {key: ingredients[key] / recipe[key] for key in ingredients if key in recipe}
        return min(dict.values())


print(recipe_batches(recipe, ingredients))