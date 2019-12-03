from aocd import data, submit


seen = {(0, 0)}
pos  = [[0, 0], [0, 0]]
turn = 0

for c in data:
    cur  = pos[turn]
    turn = 0 if turn else 1
    if   c == "^": cur[1] -= 1
    elif c == "v": cur[1] += 1
    elif c == "<": cur[0] -= 1
    elif c == ">": cur[0] += 1
    seen.add(tuple(cur))

result = len(seen)
print("result", result)
submit(result)

