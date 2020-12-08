from aocd import data, submit


data = [[line[:1], int(line[4:])] for line in data.split("\n")]

for i, _d in enumerate(data):
    if _d[0] == 'a': continue

    local = [[line[0], line[1], True] for line in data]
    local[i][0] = 'j' if local[i][0] == 'n' else 'n'
    acc = pos = 0

    while pos < len(local) and local[pos][2]:
        local[pos][2] = False
        instruction = local[pos][0]
        argument = local[pos][1]

        if   instruction == 'n': pass
        elif instruction == 'j': pos += argument; continue
        elif instruction == 'a': acc += argument
        else : ValueError(f"Unexpected instruction {instruction}")

        pos += 1

    if pos == len(local):
        print(acc)
        submit(acc)
        break

