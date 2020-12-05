from aocd import data, submit


data = (data.replace("F", "0").replace("B", "1")
            .replace("L", "0").replace("R", "1")
            .split("\n"))

result = max(int("0b" + s[:-3], 2) * 8 + int("0b" + s[-3:], 2) for s in data)
print(result)
submit(result)

