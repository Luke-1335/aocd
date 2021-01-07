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

tiles = [tiles, dict(tiles)]
additional_checks = set()

for i in range(100):
    additional_checks.clear()
    cur_tiles = tiles[i % 2 == 0 + 0]
    new_tiles = tiles[i % 2 == 0 + 1]

    for tile, black in cur_tiles.items():
        blacks = 0

        for off in directions.values():
            n_tile = (tile[0] + off[0], tile[1] + off[1])
            try: blacks += cur_tiles[n_tile]
            except KeyError: additional_checks.add(n_tile)

        if black and (blacks == 0 or blacks > 2): new_tiles[tile] = False
        elif not black and blacks == 2: new_tiles[tile] = True
        else: new_tiles[tile] = black

    for tile in additional_checks:
        blacks = 0

        for off in directions.values():
            n_tile = (tile[0] + off[0], tile[1] + off[1])
            try: blacks += cur_tiles[n_tile]
            except KeyError: pass

        new_tiles[tile] = blacks == 2


result = sum(val for val in new_tiles.values())
print(result)
submit(result)

