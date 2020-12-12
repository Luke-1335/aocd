from aocd import data, submit


ship = [ 0, 0]
wp   = [10, 1]

for d in data.split("\n"):
    action = d[0]
    value  = int(d[1:])

    if   action == "N": wp[1] += value
    elif action == "S": wp[1] -= value
    elif action == "E": wp[0] += value
    elif action == "W": wp[0] -= value

    elif action == "L" or action == "R":
        value %= 360
        if action == "R": value = 360 - value

        if   value ==  90: wp = [-wp[1],  wp[0]]
        elif value == 180: wp = [-wp[0], -wp[1]]
        elif value == 270: wp = [ wp[1], -wp[0]]

    elif action == "F":
        ship[0] += wp[0] * value
        ship[1] += wp[1] * value

    else: raise ValueError(f"Unexpected action {action}")

result = abs(ship[0]) + abs(ship[1])
print(result)
submit(result)

