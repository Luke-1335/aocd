from aocd import data, submit
from functools import reduce


tiles = {}
directions = {"se": ( 0, 1), "ne": (1, -1), "e": ( 1, 0),
              "sw": (-1, 1), "nw": (0, -1), "w": (-1, 0)}

for line in data.split("\n"):
    counts = {k: line.count(k) for k in directions}
    counts["w"] -= counts["sw"] + counts["nw"]
    counts["e"] -= counts["se"] + counts["ne"]

    tile = reduce(lambda tile, key: (tile[0] + directions[key][0] * counts[key],
                                     tile[1] + directions[key][1] * counts[key]),
                  directions, (0, 0))

    try: tiles[tile] = not tiles[tile]
    except KeyError: tiles[tile] = True

result = sum(val for val in tiles.values())
print(result)
submit(result)

