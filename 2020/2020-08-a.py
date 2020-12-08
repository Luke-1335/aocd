from aocd import data, submit


data = [[line[:1], int(line[4:]), True] for line in data.split("\n")]
acc = pos = 0

while data[pos][2]:
    data[pos][2] = False
    instruction = data[pos][0]

    if   instruction == 'n': pass
    elif instruction == 'j': pos += data[pos][1]; continue
    elif instruction == 'a': acc += data[pos][1]
    else : raise ValueError(f"Unexpected instruction {instruction}")

    pos += 1

print(acc)
submit(acc)

