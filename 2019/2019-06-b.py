from aocd import data, submit
data = data.split("\n")


class Node:
    def __init__(self, nid, parent=None):
        self.nid = nid
        self.parent = parent
        self.childs = set()

#1. fill nodes:
nodes = {}
for row in data:
    a, b = row.split(")")

    if a not in nodes: nodes[a] = Node(a)

    if b not in nodes: nodes[b] = Node(b, nodes[a])
    elif not nodes[b].parent: nodes[b].parent = nodes[a]

    nodes[a].childs.add(nodes[b])

#2. search from YOU to SAN:
result = 0
seen = set()
to_search = list({nodes["YOU"].parent} | nodes["YOU"].childs)
while to_search:
    result += 1
    new_search = []
    for node in to_search:
        if node.nid == "SAN":
            print("result", result - 2)
            submit(result)
            exit()

        elif node in seen: continue

        else:
            seen.add(node)
            new_search += list({node.parent} | node.childs)
    to_search = new_search

