from aocd import data, submit


data = data.split("\n")

instructions = (
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
)

x_max = len(data[0])
result = 1

for ix, iy in instructions:
    local = x = 0

    for y in range(iy, len(data), iy):
        x = (x + ix) % x_max
        local += data[y][x] == "#"

    result *= local

print("result", result)
submit(result)

