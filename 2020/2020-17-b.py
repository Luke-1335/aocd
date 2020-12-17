from aocd import data, submit
from itertools import product
from copy import deepcopy


data = data.split("\n")

cycles = 6

init_dim = (1, 1, len(data), len(data[0]))
dim = tuple(i + 2 * (cycles + 1) for i in init_dim)

space = [[], [[[[0 for x in range(dim[-1])] for y in range(dim[-2])] for z in range(dim[-3])] for w in range(dim[-4])]]
space[0] = deepcopy(space[1])


for (dy, y), (dx, x) in product(enumerate(range(cycles + 1, cycles + 1 + init_dim[-2])),
                                enumerate(range(cycles + 1, cycles + 1 + init_dim[-1]))):
    space[0][dim[0] // 2][dim[1] // 2][y][x] = int(data[dy][dx] == "#")


result = 0
for c in range(cycles):
    cur_state = space[(c + 0) % 2]
    new_state = space[(c + 1) % 2]

    for w, z, y, x in product(*(range(cycles - c, cycles + d + c + 2) for d in init_dim)):
        cur_ranges = (range(coord - 1, coord + 2) for coord in (w, z, y, x))
        active = sum(cur_state[nw][nz][ny][nx] for nw, nz, ny, nx in product(*cur_ranges)) - cur_state[w][z][y][x]

        if cur_state[w][z][y][x] and not (1 < active < 4): new_state[w][z][y][x] = 0
        elif not cur_state[w][z][y][x] and active == 3: new_state[w][z][y][x] = 1
        else: new_state[w][z][y][x] = cur_state[w][z][y][x]
        result += (c+1) // cycles * new_state[w][z][y][x]

print(result)
submit(result)

