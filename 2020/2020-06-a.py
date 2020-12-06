from aocd import data, submit


seen = set()
result = 0

for line in data.split("\n") + [""]:
    if line == "":
        result += len(seen)
        seen = set()
    seen |= set(line)

print(result)
submit(result)

