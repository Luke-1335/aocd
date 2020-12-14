from aocd import data, submit


memory = {}

for row in data.split("\n"):
    if row[1] == "a":
        mask = row[7:]
        or_mask  = int("0b" + mask.replace("X", "0"), 2)
        and_mask = int("0b" + mask.replace("X", "1"), 2)

    elif row[1] == "e":
        address = int(row[4 : row.index("]")])
        value = int(row[row.index("=") + 2:])
        memory[address] = value & and_mask | or_mask

    else: raise ValueError(f"Unexpected instruction {row}")

result = sum(memory.values())
print(result)
submit(result)

