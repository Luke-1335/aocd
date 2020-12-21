from aocd import data, submit


allergens = {}

for line in data.split("\n"):
    food_ingredients, food_allergens = line.split(" (contains ")

    food_ingredients = food_ingredients.split(" ")
    food_allergens = food_allergens[:-1].split(", ")

    for a in food_allergens:
        try: allergens[a] &= set(food_ingredients)
        except KeyError: allergens[a] = set(food_ingredients)

while any(len(a) > 1 for a in allergens.values()):
    for i1 in allergens.values():
        if len(i1) != 1: continue
        for i2 in allergens.values():
            if i1 == i2: continue
            i2.discard(list(i1)[0])

result = ",".join(list(v)[0] for k, v in sorted(allergens.items()))
print(result)
submit(result)

