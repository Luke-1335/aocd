from aocd import data, submit


result = 0
for line in data.split("\n"):
    count, letter, password = line.split(" ")
    count = tuple(int(n) - 1 for n in count.split("-"))
    result += (password[count[0]] == letter[0]) ^ (password[count[1]] == letter[0])

print("result", result)  
submit(result)

