from aocd import data, submit


lvl = 0
for i, c in enumerate(data, start=1):
    lvl += 1 if c == "(" else -1
    if lvl == -1:
        print("result", i)
        submit(i)
        break

