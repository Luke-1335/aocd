from aocd import data, submit


allergens = {}
ingredients = {}

for line in data.split("\n"):
    food_ingredients, food_allergens = line.split(" (contains ")

    food_ingredients = food_ingredients.split(" ")
    food_allergens = food_allergens[:-1].split(", ")

    for i in food_ingredients:
        try: ingredients[i] += 1
        except KeyError: ingredients[i] = 1

    for a in food_allergens:
        try: allergens[a] &= set(food_ingredients)
        except KeyError: allergens[a] = set(food_ingredients)

for allergenic_ingredients in allergens.values():
    for ai in allergenic_ingredients: ingredients[ai] = 0

result = sum(ingredients.values())
print(result)
submit(result)

