from aocd import data, submit
data = [int(d) for d in data.split("-")]


result = 0
for num in range(data[0], data[1]):
    val = str(num)
    valid = False
    for a, b in zip(val, val[1:]):
        a = int(a)
        b = int(b)
        if a == b: valid = True
        if a > b: break
    else:
        result += valid

print("result", result)
submit(result)

