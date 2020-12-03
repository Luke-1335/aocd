from aocd import data, submit


data  = data.split("\n")[1:]
x_max = len(data[0])

result = x = 0

for row in data:
    x = (x + 3) % x_max
    result += row[x] == "#"

print("result", result)
submit(result)

