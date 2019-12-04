from aocd import data, submit
data = [int(d) for d in data.split("-")]


result = 0
for num in range(data[0], data[1]):
    val   = str(num)
    chars = set(val)
    if not any([val.count(c) == 2 for c in chars]):
        continue

    for a, b in zip(val, val[1:]):
        a = int(a)
        b = int(b)
        if a > b: break
    else:
        result += 1

print("result", result)
submit(result)

