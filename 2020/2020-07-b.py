from aocd import data, submit


childs = {}

def accumulate(bag, mult):
    return sum(mult * (count + accumulate(child, count)) for child, count in childs[bag].items())

for line in data.split("\n"):
    parent, childs_str = line.split(" bags contain ")
    childs[parent] = {}

    for child_str in childs_str.split(", "):
        if child_str == "no other bags.": continue

        i_count = child_str.find(" ")
        i_color = child_str.find(" bag")
        child = child_str[i_count+1 : i_color]

        childs[parent][child] = int(child_str[:i_count])

result = accumulate("shiny gold", 1)
print(result)
submit(result)

