from aocd import data, submit


deck1, deck2 = (list(map(int, deck.split("\n")[1:])) for deck in data.split("\n\n"))

while deck1 and deck2:
    if deck1[0] > deck2[0]:
        deck1.extend((deck1.pop(0), deck2.pop(0)))
    else:
        deck2.extend((deck2.pop(0), deck1.pop(0)))

winner = deck1 if deck1 > deck2 else deck2
result = sum(i * val for i, val in enumerate(winner[::-1], 1))

print(result)
submit(result)

