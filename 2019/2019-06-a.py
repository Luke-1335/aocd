from aocd import data, submit
data = data.split("\n")


def sum_nodes(n, nodes):
    return len(nodes[n]) + sum([sum_nodes(c, nodes) for c in nodes[n] if c in nodes])


nodes = {}
for row in data:
    a, b = row.split(")")
    try:
        nodes[a].append(b)
    except KeyError:
        nodes[a] = []
        nodes[a].append(b)

result = sum([sum_nodes(n, nodes) for n in nodes])
print("result", result)
submit(result)

