from aocd import data, submit


data = data.split("\n") + [""]

required = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
required = {key: False for key in required}
valid = 0

for row in data:
    if row == "":
        valid += all(val for val in required.values())
        required = {key: False for key in required}

    for key in required:
        if key + ":" in row: required[key] = True

print("result", valid)
submit(valid)

