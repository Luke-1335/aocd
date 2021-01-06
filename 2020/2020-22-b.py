from aocd import data, submit


deck1, deck2 = (list(map(int, deck.split("\n")[1:])) for deck in data.split("\n\n"))

def play(deck1, deck2, cache={}):
    state = tuple(deck1 + [-1] + deck2)
    if state in cache: return cache[state]

    seen1 = set()
    seen2 = set()

    while deck1 and deck2:
        if tuple(deck1) in seen1 and tuple(deck2) in seen2:
            cache[state] = True
            return True

        seen1.add(tuple(deck1))
        seen2.add(tuple(deck2))

        v1 = deck1.pop(0)
        v2 = deck2.pop(0)

        round_winner = v1 > v2 if v1 > len(deck1) or v2 > len(deck2) else play(deck1[:v1], deck2[:v2], cache)

        if round_winner: deck1.extend((v1, v2))
        else: deck2.extend((v2, v1))

    cache[state] = deck1 > deck2
    return deck1 > deck2

play(deck1, deck2)
winner = deck1 if deck1 > deck2 else deck2
result = sum(i * val for i, val in enumerate(winner[::-1], 1))

print(result)
submit(result)

