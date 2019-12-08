from aocd import data


zeros  = []
layers = []
w, h = 25, 6
layer = [[ "2" for x in range(w)] for y in range(h)]

for i, c in enumerate(data):
    y = i//w%h
    x = i%w
    if layer[y][x] == "2": layer[y][x] = c

for y in range(h):
    for x in range(w):
        print(" " if layer[y][x] == "0" else "#", end = "")
    print()

