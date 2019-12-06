from aocd import data, submit
from collections import OrderedDict


result = 0
for row in data.split("\n"):
    row   = row.split("-")
    check = row[-1].split("[")[-1][:-1]
    sid   = int(row[-1].split("[")[0])
    name  = "".join(row[:-1]) #name is string without dashes

    name = "".join(OrderedDict.fromkeys(sorted(name, key=lambda c: (-name.count(c), c))))
    if all([c[0] == c[1] for c in zip(name, check)]): result += sid

print("result", result)
submit(result)

