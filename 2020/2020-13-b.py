from aocd import data, submit


bus_ids = [(int(bus), i) for i, bus in enumerate(data.split("\n")[1].split(",")) if bus != "x"]

result = 0
mult = 1

for bus in bus_ids:
    while (bus[1] + result) % bus[0]: result += mult
    mult *= bus[0]

print(result)
submit(result)

