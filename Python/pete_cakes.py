"""
Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. 
Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and
 returns the maximum number of cakes Pete can bake (integer). 
 For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200).
  Ingredients that are not present in the objects, can be considered as 0.

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
"""

import enum


bunch = [{'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}]
bunch2 = [{'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, {'sugar': 500, 'flour': 2000, 'milk': 2000}]
cakes = 0
        
recipe = bunch[0]
ingr = bunch[1]

recipe = bunch2[0]
ingr = bunch2[1]

maximum = []
for a in recipe:
    if a not in ingr or recipe[a] > ingr[a]:
        print('No')
    else:
        maximum.append(ingr[a] // recipe[a])
print(min(maximum))

# maxi = [ingr[a] // recipe[a] for a in recipe if a in ingr and recipe[a] < ingr[a]]
maxi = [ingr[a] // recipe[a] if a in ingr and recipe[a] < ingr[a] else 0 for a in recipe]
# maxi = [a if a not in ingr for a in recipe]

print(0 if False in maxi else min(maxi))