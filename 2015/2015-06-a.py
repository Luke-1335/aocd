from aocd import data, submit
from itertools import product


lights_on = set()
for row in data.split("\n"):
    row = row[6:]
    if   row[0] == "f": op = lights_on.discard
    elif row[0] == "n": op = lights_on.add
    else: op = None

    row = row.split(" ")
    x0, y0 = map(int, row[1].split(","))
    x1, y1 = map(int, row[3].split(","))

    for pt in product(range(x0, x1+1), range(y0, y1+1)):
        if op: op(pt)
        else:
            if (pt) in lights_on:
                lights_on.discard(pt)
            else:
                lights_on.add(pt)

result = len(lights_on)
print("result", result)
submit(result)

