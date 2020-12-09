from aocd import data, submit


data = [int(d) for d in data.split("\n")]
preamble = 25

for i, number in enumerate(data[preamble:]):
    valid = {data[a] + data[b] for a in range(i, i + preamble) for b in range(i + 1, i + preamble)}
    if number not in valid: break

print(number)
submit(number)

