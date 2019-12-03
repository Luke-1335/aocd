from aocd import data, submit
lines  = data.split("\n")
result = 0


for line in lines:
    val = int(line)
    while True:
        val = val // 3 - 2
        if val <= 0: break
        result += val 


print("result", result)
submit(result)

