from aocd import data, submit


data = data.split("\n")
timestamp = int(data[0])
bus_ids = [int(bus) for bus in data[1].split(",") if bus != "x"]

result = min(((bus - timestamp % bus, bus) for bus in bus_ids))
result = result[0] * result[1]

print(result)
submit(result)

