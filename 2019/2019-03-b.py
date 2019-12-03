from aocd import data, submit
data = data.split("\n")


LARGE = 2**128
seen = {(0, 0): [0, LARGE]}

for i in range(2):
    pos  = [0, 0]
    dist = 0
    for val in data[i].split(","):
        dir  = val[0]
        step = int(val[1:])

        while step > 0:
            step -= 1
            dist += 1
            if   dir == "U": pos[1] -= 1
            elif dir == "D": pos[1] += 1
            elif dir == "L": pos[0] -= 1
            elif dir == "R": pos[0] += 1

            npos = (pos[0], pos[1])
            if   i == 1 and npos in seen:
                seen[npos][1] = min(seen[npos][1], dist)   
            elif i == 0 and npos not in seen:
                seen[npos] = [dist, LARGE]

result = min([sum(dist) for dist in seen.values()])
print("result", result)
submit(result)

