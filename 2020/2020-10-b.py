from aocd import data, submit


data = [0] + sorted([int(d) for d in data.split("\n")])
data.append(data[-1])

mults = (1, 1, 2, 4, 7)
result = 1
i = 0

while i < len(data) - 1:
    next = 1
    while data[i + next] - data[i] == next: next += 1

    result *= mults[next - 1]
    i += next

print(result)
submit(result)

