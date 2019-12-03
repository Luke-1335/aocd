from aocd import data, submit


instructions = [int(line) for line in data.split("\n")]
freq, i = 0, -1
seen = set()

while freq not in seen:
    seen.add(freq)
    i = (i + 1) % len(instructions)
    freq += instructions[i]

print("result", freq)
submit(freq)

