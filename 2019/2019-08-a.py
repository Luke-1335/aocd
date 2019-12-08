from aocd import data, submit


ilen = 25 * 6

n = [ (data[i:i+ilen].count("0"),
       data[i:i+ilen].count("1"),
       data[i:i+ilen].count("2"))
     for i in range(0, len(data), ilen) ]

n.sort()
result = n[0][1] * n[0][2]
print("result", result)
submit(result)

