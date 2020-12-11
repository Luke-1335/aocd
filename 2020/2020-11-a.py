from aocd import data, submit


data = [[[c for c in row] for row in data.split("\n")], []]
data[1] = [["." for c in row] for row in data[0]]

count_ocupied = lambda x, y, state: sum(
    -1 < (x + px) < len(state[y]) and
    -1 < (y + py) < len(state) and
    state[y + py][x + px] == "#"
    for px, py in ((-1, -1), ( 0, -1), (+1, -1), (-1,  0),
                   (+1,  0), (-1, +1), ( 0, +1), (+1, +1))
)


i = 0

while True:
    i += 1
    cur_state = data[(i + 1) % 2]
    new_state = data[i % 2]

    for y, row in enumerate(cur_state):
        for x, val in enumerate(row):
            if val == ".": continue

            ocupied = count_ocupied(x, y, cur_state)

            if   val == "L" and ocupied == 0: new_state[y][x] = "#"
            elif val == "#" and ocupied >= 4: new_state[y][x] = "L"
            else: new_state[y][x] = val

    if cur_state == new_state: break

result = sum(val == "#" for row in data[0] for val in row)
print(result)
submit(result)

