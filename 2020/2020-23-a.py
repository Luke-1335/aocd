from aocd import data, submit


data = list(map(int, data))
cur = 0

for _ in range(100):
    cur_cap = data[cur]

    beg = (cur + 1) % len(data)
    end = (beg + 3) % len(data)

    if beg > end:
        pick_up = data[beg:] + data[:end]
        data = data[end:beg]
    else:
        pick_up = data[beg:end]
        data = data[:beg] + data[end:]

    cur = data.index(cur_cap)
    destination = data[cur] - 1
    while destination and destination in pick_up: destination -= 1
    if not destination: destination = 9
    while destination in pick_up: destination -= 1

    i = 1 + data.index(destination)
    data = data[:i] + pick_up + data[i:]
    cur = (1 + data.index(cur_cap)) % len(data)


i = 1 + data.index(1)
result = "".join(map(str, data[i:] + data[:i-1]))

print(result)
submit(result)

