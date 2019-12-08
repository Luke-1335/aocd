from aocd import data, submit
from string import ascii_lowercase as alphabet


def react(polymer):
    i = 0
    while i+1 < len(polymer):
        if polymer[i].lower() == polymer[i+1].lower() and polymer[i] != polymer[i+1]:
            polymer = polymer[:i] + polymer[i+2:]
            i -= i > 0
            continue
        i += 1
    return len(polymer)

result = min([react(data.replace(c, "").replace(c.upper(), "")) for c in alphabet])
print("result", result)
submit(result)

