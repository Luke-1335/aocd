from aocd import data, submit
lines = data.split("\n")


result = 0
for line in lines:
    l, w, h = map(int, line.split("x"))
    sides   = (l*w, l*h, w*h)
    result += 2*sum(sides) + min(sides)

print("result", result)
submit(result)

