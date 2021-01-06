from aocd import data, submit


def process_group(group):
    while True:
        i_mult = group.find("*")
        i_plus = group.find("+")
        i = min(i_mult, i_plus)

        if i == -1: i = max(i_mult, i_plus)
        if i == -1: return group

        op = group[i]

        d1 = 0
        try:
            while i - d1 >= 0:
                d1 += 1
                n1 = int(group[i - d1 : i])

        except ValueError: d1 -= 1

        d2 = 1
        try:
            while i + d2 < len(group):
                n2 = int(group[i + 1 : i + 1 + d2])
                d2 += 1

        except ValueError: d2 -= 1

        group = group[ : i - d1] + str(n1 * n2 if op == "*" else n1 + n2) + group[i + 1 + d2 : ]

result = 0

for line in data.split("\n"):
    line = "(" + line.replace(" ", "") + ")"

    while True:
        e = line.find(")")
        s = line[:e].rfind("(") + 1
        if e == -1: break

        line = line[ : s - 1] + process_group(line[s : e]) + line[e + 1 : ]

    result += int(line)

print(result)
submit(result)

