from aocd import data, submit


data = [int(d) for d in data.split("\n")]
preamble = 25

for i, number in enumerate(data[preamble:]):
    valid = {data[a] + data[b] for a in range(i, i + preamble) for b in range(i + 1, i + preamble)}
    if number not in valid: break

s = e = result = 0

while result != number:
    if result > number:
        result -= data[s]
        s += 1
    else:
        result += data[e]
        e += 1

result = max(data[s:e]) + min(data[s:e])
print(result)
submit(number)

