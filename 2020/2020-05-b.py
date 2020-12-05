from aocd import data, submit


data = (data.replace("F", "0").replace("B", "1")
            .replace("L", "0").replace("R", "1")
            .split("\n"))

data = sorted(int("0b" + s[:-3], 2) * 8 + int("0b" + s[-3:], 2) for s in data)

for i, d in enumerate(data[:-1]):
    if d + 1 != data[i + 1]:
        result = d + 1
        break

print(result)
submit(result)

