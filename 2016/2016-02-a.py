from aocd import data, submit


pos = [1, 1]
result = ""

for line in data.split("\n"):
    for i in line:
        if   i == "U" or i == "D":
            pos[1] += -1 if i == "U" else 1
        else:
            pos[0] += -1 if i == "L" else 1
        
        for p in (0, 1):
            if   pos[p] < 0: pos[p] = 0
            elif pos[p] > 2: pos[p] = 2
  
    result += str(3*pos[1] + 1+pos[0])

    
print("result", result)
submit(result)

