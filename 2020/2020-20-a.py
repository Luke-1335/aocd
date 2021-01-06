from aocd import data, submit


blocks = {b[0][5:]: b[1].split("\n") for b in (block.split(":\n") for block in data.split("\n\n"))}

for k, v in blocks.items():
    blocks[k] = [v[0], v[-1], "".join(a[0] for a in v), "".join(a[-1] for a in v)]


result = 1
for b_id1, sides1 in blocks.items():
    options = [0, 0, 0, 0]

    for b_id2, sides2 in blocks.items():
        if b_id1 == b_id2: continue

        for i, s1 in enumerate(sides1):
            if s1 in sides2: options[i] += 1
            if s1[::-1] in sides2: options[i] += 1

    if sum(options) == 2: result *= int(b_id1)


print(result)
submit(result)

