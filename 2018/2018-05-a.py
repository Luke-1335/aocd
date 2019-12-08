from aocd import data, submit


i = 0
while i+1 < len(data):
    if data[i].lower() == data[i+1].lower() and data[i] != data[i+1]:
        data = data[:i] + data[i+2:]
        i -= i > 0
        continue
    i += 1

result = len(data)
print("result", result)
submit(result)

