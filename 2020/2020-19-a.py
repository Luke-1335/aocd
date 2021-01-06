from aocd import data, submit
from itertools import product


rules, data = data.split("\n\n")

rules = {k: [n.replace("\"", "").split(" ") for n in v.split(" | ")] for k, v in (r.split(": ") for r in rules.split("\n"))}
cache = {}

def solve_rule(r_id):
    if r_id in cache: return cache[r_id]

    rule = rules[r_id]
    result = []

    for part in rule:
        part_result = []

        for sub in part:
            if sub in cache:  part_result.append(cache[sub])
            elif sub in "ab": part_result.append((sub,))
            else:             part_result.append(solve_rule(sub))

        result += list("".join(i) for i in product(*part_result))

    cache[r_id] = result
    return result


possible = set(solve_rule("0"))
result = sum(d in possible for d in data.split("\n"))
print(result)
submit(result)

