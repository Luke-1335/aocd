from aocd import data, submit


data = [0] + sorted([int(d) for d in data.split("\n")])

diff_1 = sum(1 for i, n in enumerate(data[:-1]) if n + 1 == data[i+1])
diff_3 = len(data) - diff_1
result = diff_1 * diff_3

print(result)
submit(result)

