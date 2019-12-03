from aocd import data, submit
lines = data.split("\n")


program = [int(val) for line in lines for val in line.split(",")]
program[1] = 12
program[2] = 2

for i in range(0, len(program), 4):
    opcode = program[i]
    if opcode == 99: break

    a = program[i+1]
    b = program[i+2]
    c = program[i+3]

    if opcode == 1:
        program[c] = program[a] + program[b]
    elif opcode == 2:
        program[c] = program[a] * program[b]
    else:
        print("wtf is this opcode?")

result = program[0]
print("result", result)
submit(result)

