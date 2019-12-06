from aocd import data, submit
from string import ascii_lowercase


letters = len(ascii_lowercase)
for row in data.split("\n"):
    sid  = int(row.split("-")[-1].split("[")[0])
    name = row[:row.rfind("-")]
    name = "".join([chr((ord(c)+sid-ord("a"))%letters+ord("a")) if c != "-" else " " for c in name])
    if "northpole" in name:
        print("result", sid)
        submit(sid)

