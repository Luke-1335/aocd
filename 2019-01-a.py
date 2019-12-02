from aocd import data, submit
lines  = data.split("\n")


result = sum([int(line) // 3 - 2 for line in lines])


print("result", result)  
submit(result)

