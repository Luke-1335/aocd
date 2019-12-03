from aocd import data, submit


seen = {(0, 0)}
pos  = [0, 0]

for c in data:
    if   c == "^": pos[1] -= 1
    elif c == "v": pos[1] += 1
    elif c == "<": pos[0] -= 1
    elif c == ">": pos[0] += 1
    seen.add(tuple(pos))

result = len(seen)
print("result", result)
exit()
submit(result)

