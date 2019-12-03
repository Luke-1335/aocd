from aocd import data, submit


result = sum([int(line) for line in data.split("\n")])


print("result", result)
submit(result)

