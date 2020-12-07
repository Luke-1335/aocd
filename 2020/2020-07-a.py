from aocd import data, submit


parents = {}

for line in data.split("\n"):
    parent, childs_str = line.split(" bags contain ")

    for child_str in childs_str.split(", "):
        if child_str == "no other bags.": continue

        i_count = child_str.find(" ")
        i_color = child_str.find(" bag")
        child = child_str[i_count+1 : i_color]

        try: parents[child].append(parent)
        except KeyError: parents[child] = [parent]

to_search = ["shiny gold"]
seen = set()

while to_search:
    try:
        child_parents = parents[to_search.pop()]
        seen |= set(child_parents)
        to_search.extend(child_parents)
    except KeyError: pass

result = len(seen)
print(result)
submit(result)

