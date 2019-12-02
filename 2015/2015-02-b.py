from aocd import data, submit
import numpy as np
lines = data.split("\n")


result = 0
for line in lines:
    lengths = [int(val) for val in line.split("x")]
    result += 2*(sum(lengths) - max(lengths)) + np.prod(lengths) 

print("result", result)  
submit(result)

