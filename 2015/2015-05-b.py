from aocd import data, submit


rule1 = lambda row: any(["".join(ab) in row[num:] for num, ab in enumerate(zip(row, row[1:-2]), start=2)])
rule2 = lambda row: any([a == b for a, b in zip(row, row[2:])])

result = sum([rule1(row) and rule2(row) for row in data.split("\n")])
print("result", result)
submit(result)

