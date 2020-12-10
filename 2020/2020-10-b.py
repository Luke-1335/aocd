from aocd import data, submit


data = [0] + sorted([int(d) for d in data.split("\n")])
data.append(data[-1])

mults = (1, 1, 2, 4, 7)
result = 1
i = 0

while i < len(data) - 1:
    in_row = 1
    while data[i + in_row] - data[i] == in_row: in_row += 1

    result *= mults[in_row - 1]
    i += in_row

print(result)
submit(result)

