from aocd import data, submit


suit = {}
for fab in data.split("\n"):
    fab = fab.split(" ")
    x, y = map(int, fab[2][:-1].split(","))
    w, t = map(int, fab[3].split("x"))
    
    for yy in range(y, y+t): 
        for xx in range(x, x+w):
            pt = (xx, yy)
            if pt in suit: suit[pt] += 1
            else:          suit[pt]  = 0
    
result = sum([n > 0 for n in suit.values()])
print("result", result)
submit(result)

