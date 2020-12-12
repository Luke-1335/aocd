from aocd import data, submit


direction = 90
position = [0, 0]

for d in data.split("\n"):
    action = d[0]
    value  = int(d[1:])

    if   action == "N": position[1] += value
    elif action == "S": position[1] -= value
    elif action == "E": position[0] += value
    elif action == "W": position[0] -= value
    elif action == "L": direction = (direction - value) % 360
    elif action == "R": direction = (direction + value) % 360
    elif action == "F": position[(direction + 90) % 180 // 90] -= (direction // 180 * 2 -1) * value

    else: raise ValueError(f"Unexpected action {action}")

result = abs(position[0]) + abs(position[1])
print(result)
submit(result)

