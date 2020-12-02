from aocd import data, submit


values = [int(val) for val in data.split("\n")]

for i, a in enumerate(values):
    for b in values[i+1:]:
        for c in values[i+2:]:
            if a + b + c != 2020: continue
            result = a * b * c
            print("result", result)  
            submit(result)
            break

