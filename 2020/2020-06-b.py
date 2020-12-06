from aocd import data, submit
from string import ascii_lowercase


seen = set(ascii_lowercase)
result = 0

for line in data.split("\n") + [""]:
    if line == "":
        result += len(seen)
        seen = set(ascii_lowercase)

    else: seen &= set(line)

print(result)
submit(result)

