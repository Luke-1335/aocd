from aocd import data, submit


data   = [ list(map(int, filter(lambda val: val != "", row.split(" ")))) for row in data.split("\n") ]
result = sum([r[0] + r[1] > r[2] and r[0] + r[2] > r[1] and r[1] + r[2] > r[0] for r in data])


print("result", result)
submit(result)

