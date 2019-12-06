from aocd import data, submit
from itertools import product
import numpy as np


lights = np.zeros((1000, 1000), dtype=np.int32)
for row in data.split("\n"):
    row = row[6:]
    if   row[0] == "f": val = -1
    elif row[0] == "n": val =  1
    else: val = 2

    row = row.split(" ")
    x0, y0 = map(int, row[1].split(","))
    x1, y1 = map(int, row[3].split(","))

    for x, y in product(range(x0, x1+1), range(y0, y1+1)):
        lights[y][x] += val
        if lights[y][x] == -1: lights[y][x] = 0

result = np.sum(lights)
print("result", result)
submit(result)

