from aocd import data, submit


rules, my_ticket, tickets = data.split("\n\n")

rules = [tuple(map(int, r.replace("-", " ").replace(" or", "").split(" ")))
         for r in (rule.split(": ")[1] for rule in rules.split("\n"))]

tickets = [tuple(map(int, row.split(","))) for row in tickets.split("\n")[1:]]


non_valid = 0
for ticket in tickets:
    for number in ticket:
        non_valid += number * (not any((r[0] <= number <= r[1] or r[2] <= number <= r[3] for r in rules)))

print(non_valid)
submit(non_valid)

