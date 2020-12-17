from aocd import data, submit


rules, my_ticket, tickets = data.split("\n\n")

rules = {rule[0]: tuple(map(int, rule[1].replace("-", " ").replace(" or", "").split(" ")))
         for rule in (row.split(": ") for row in rules.split("\n"))}

my_ticket = tuple(map(int, my_ticket.split("\n")[1].split(",")))

tickets = [tuple(map(int, row.split(","))) for row in tickets.split("\n")[1:]]

options = [set(rules) for number in my_ticket]


for ticket in tickets:
    if all(any(rule[0] <= num <= rule[1] or rule[2] <= num <= rule[3] for rule in rules.values()) for num in ticket):
        for i, num in enumerate(ticket):
            options[i] &= {name for name, rule in rules.items() if rule[0] <= num <= rule[1] or rule[2] <= num <= rule[3]}

while any(len(opt) > 1 for opt in options):
    for o1 in options:
        if len(o1) != 1: continue
        for o2 in options:
            if o1 == o2: continue
            o2.discard(list(o1)[0])

result = 1
for i, opt in enumerate(options):
    result *= my_ticket[i] ** ("departure" in list(opt)[0])

print(result)
submit(result)

