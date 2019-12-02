from aocd import data, submit


keys = [ ["-", "-", "-", "-", "-", "-", "-"],
         ["-", "-", "-", "1", "-", "-", "-"],
         ["-", "-", "2", "3", "4", "-", "-"],
         ["-", "5", "6", "7", "8", "9", "-"],
         ["-", "-", "A", "B", "C", "-", "-"],
         ["-", "-", "-", "D", "-", "-", "-"],
         ["-", "-", "-", "-", "-", "-", "-"] ]

pos = [3, 3]
result = ""

for line in data.split("\n"):
    for i in line:
        if   i == "U": pos[1] -= 1 if keys[pos[1]-1][pos[0]  ] != "-" else 0
        elif i == "D": pos[1] += 1 if keys[pos[1]+1][pos[0]  ] != "-" else 0
        elif i == "L": pos[0] -= 1 if keys[pos[1]  ][pos[0]-1] != "-" else 0
        elif i == "R": pos[0] += 1 if keys[pos[1]  ][pos[0]+1] != "-" else 0

    result += keys[pos[1]][pos[0]]

print("result", result)
submit(result)

