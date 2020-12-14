from itertools import combinations
from aocd import data, submit
import re


memory = {}

for row in data.split("\n"):
    if row[1] == "a":
        mask = row[7:]
        and_mask = int("0b" + mask.replace("0", "1").replace("X", "0"), 2)
        or_mask  = int("0b" + mask.replace("X", "0"), 2)
        indexes  = [m.start() for m in re.finditer("X", mask)]

    elif row[1] == "e":
        address = int(row[4 : row.index("]")]) & and_mask | or_mask
        value = int(row[row.index("=") + 2 : ])

        for i in range(len(indexes) + 1):
            comb = combinations(indexes, i)

            for combination in list(comb):
                mask = ["0" for _ in range(36)]
                for c in combination: mask[c] = "1"
                memory[address | int("0b" + "".join(mask), 2)] = value

    else: raise ValueError(f"Unexpected instruction {row}")

result = sum(memory.values())
print(result)
submit(result)

