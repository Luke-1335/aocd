from aocd import data, submit


zeros  = []
layers = []
w, h, z = 25, 6, 0

create_layer = lambda: [[ None for x in range(w)] for y in range(h)]
layer = create_layer()

for i, c in enumerate(data):
    if i % (w*h) == 0 and i:
        layers.append(layer)
        zeros.append(z)
        layer, z = create_layer(), 0

    z += c == "0"
    layer[i//w%h][i%w] = c

layers.append(layer)
zeros.append(z)


min_i = zeros.index(min(zeros)) #another exmaple of an efficiency :D
ones, twos = 0, 0
for y in range(h):
    ones += layers[min_i][y].count("1")
    twos += layers[min_i][y].count("2")

result = ones * twos
print("result", result)
submit(result)

