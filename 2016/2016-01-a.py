from aocd import data, submit

dirs = [0, 0, 0, 0]
i = 0

for instruction in data.split(", "):
    side = 1 if instruction[0] == "R" else -1
    step = int(instruction[1:])
    i = (i + side) % 4
    dirs[i] += step   

result = abs(dirs[0] - dirs[2]) + abs(dirs[1] - dirs[3])
print("result", result)  
submit(result)

