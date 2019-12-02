from aocd import data, submit
lines = data.split("\n")


d, t = 0, 0
for line in lines:
    chars = {}
    for c in line:
        try:
            chars[c] += 1
        except KeyError:
            chars[c] = 1
            
    d += any([val == 2 for val in chars.values()])
    t += any([val == 3 for val in chars.values()])

result = d * t
print("result", result)  
submit(result)

