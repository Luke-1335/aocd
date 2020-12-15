from aocd import data, submit


data = [int(d) for d in data.split(",")]
spoken = {number: turn for turn, number in enumerate(data, 1)}
number = data[-1]
turn = len(spoken)

while turn < 30000000:
    try: last = spoken[number]
    except KeyError: last = turn
    spoken[number] = turn
    number = turn - last
    turn += 1

print(number)
submit(number)

