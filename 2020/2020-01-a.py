from aocd import data, submit


values = [int(val) for val in data.split("\n")]

for i, a in enumerate(values):
    for b in values[i+1:]:
        if a + b != 2020: continue
        result = a * b
        print("result", result)  
        submit(result)
        break

