from aocd import data, submit
from datetime import datetime


def process_row(string):
    date = datetime.strptime(string[:18], "[%Y-%m-%d %H:%M]")
    if   "wakes"  in string: return (date, "w")
    elif "asleep" in string: return (date, "s")
    else: return  (date, "".join(c for c in string[18:] if c.isdigit()))


entries = [process_row(row) for row in data.split("\n")]
entries.sort()
guards = {}
gid, start = "", 0

for entry in entries:
    if "w" == entry[1]:
        end = entry[0].minute
        if gid not in guards:
            guards[gid] = [0] * 60

        for m in range(start, end):
            guards[gid][m] += 1

    elif "s" == entry[1]:
        start = entry[0].minute
    else:
        gid = entry[1]

gids = [ max(guards, key=lambda gid: sum(guards[gid])),
         max(guards, key=lambda gid: max(guards[gid])) ]

for i, part in enumerate(["a", "b"]):
    gid = gids[i]
    result = int(gid) * guards[gid].index(max(guards[gid]))
    print(f"result {part}", result)
    submit(result)

