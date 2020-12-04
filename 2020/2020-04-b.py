from aocd import data, submit


data = data.split("\n") + [""]

validate = {
    "byr": lambda val: 1920 <= int(val) <= 2002,
    "iyr": lambda val: 2010 <= int(val) <= 2020,
    "eyr": lambda val: 2020 <= int(val) <= 2030,
    "hgt": lambda val: (
        (150 if val[-2:] == "cm" else 59)
        <= int(val[:-2]) <=
        (193 if val[-2:] == "cm" else 76)
    ),
    "hcl": lambda val: val[0] == "#" and int(val[1:], 16) >= 0,
    "ecl": lambda val: val in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
    "pid": lambda val: len(val) == 9 and val.isdecimal(),
}

required = {key: False for key in validate}
valid = 0

for row in data:
    if row == "":
        valid += all(val for val in required.values())
        required = {key: False for key in required}

    for entry in row.split(" "):
        try:
            key, val = entry.split(":")
            required[key] = validate[key](val)
        except (ValueError, KeyError): pass

print("result", valid)
submit(valid)

