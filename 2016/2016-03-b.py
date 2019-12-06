from aocd import data, submit
import numpy as np


data   = np.concatenate([row for row in np.transpose([ list(map(int, filter(lambda val: val != "", row.split(" ")))) for row in data.split("\n") ])])
data   = [data[i:i+3] for i in range(0, len(data),3)]
result = sum([r[0] + r[1] > r[2] and r[0] + r[2] > r[1] and r[1] + r[2] > r[0] for r in data])


print("result", result)
submit(result)

