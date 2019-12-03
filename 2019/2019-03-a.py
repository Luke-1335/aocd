from aocd import data, submit
data = data.split("\n")


seen = {(0, 0)}
intersections = []

for i in range(2):
    pos = [0, 0]
    for val in data[i].split(","):
        way  = val[0]
        step = int(val[1:])

        while step > 0:
            step -= 1
            if   way == "U": pos[1] -= 1
            elif way == "D": pos[1] += 1
            elif way == "L": pos[0] -= 1
            elif way == "R": pos[0] += 1

            npos = (pos[0], pos[1])
            if i == 1 and npos in seen:
                intersections.append(npos)
            elif i == 0:
                seen.add(npos)

result = min([abs(pt[0]) + abs(pt[1]) for pt in intersections])
print("result", result)
submit(result)

