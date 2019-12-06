from aocd import data, submit


rule1 = lambda row: 3 <= sum([row.count(c) for c in "aeiou"])
rule2 = lambda row: any([a == b for a, b in zip(row, row[1:])])
rule3 = lambda row: all([bad not in row for bad in ["ab", "cd", "pq", "xy"]])

result = sum([rule1(row) and rule2(row) and rule3(row) for row in data.split("\n")])
print("result", result)
submit(result)

