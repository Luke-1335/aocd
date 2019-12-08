from aocd import data, submit


ilen = 25 * 6
get_counts = lambda s: (s.count("0"), s.count("1"), s.count("2"))
n = [ get_counts(data[i:i+ilen]) for i in range(0, len(data), ilen) ]

n.sort()
result = n[0][1] * n[0][2]
print("result", result)
submit(result)

