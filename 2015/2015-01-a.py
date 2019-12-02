from aocd import data, submit


result = sum([1 if c == "(" else -1 for c in data])


print("result", result)  
submit(result)

