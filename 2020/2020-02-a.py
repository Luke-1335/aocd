from aocd import data, submit


result = 0
for line in data.split("\n"):
    count, letter, password = line.split(" ")
    count = tuple(int(n) for n in count.split("-"))
    result += count[0] <= password.count(letter[0]) <= count[1]

print("result", result)  
submit(result)

