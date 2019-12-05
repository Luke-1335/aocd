from aocd import data, submit
from hashlib import md5
data = data.encode()


i = 0
for i in range(2**64):
    val  = data + str(i).encode()
    hash = md5(val)
    if hash.hexdigest()[:6] == "000000": break

print("result", i)
submit(i)

