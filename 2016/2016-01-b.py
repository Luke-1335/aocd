from aocd import data, submit

visited = set()
dirs = [0, 0, 0, 0]
i = 0

for instruction in data.split(", "):
    side = 1 if instruction[0] == "R" else -1
    step = int(instruction[1:])
    i = (i + side) % 4
    
    while step > 0:
        dirs[i] += 1
        pos = (dirs[0] - dirs[2], dirs[1] - dirs[3])
 
        if (pos in visited): 
            result = abs(dirs[0] - dirs[2]) + abs(dirs[1] - dirs[3])
            print("result", result)  
            submit(result)
            exit()
        else:
            visited.add(pos)
            step -= 1

