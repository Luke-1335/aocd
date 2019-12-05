from aocd import data, submit
program = [int(d) for d in data.split(",")]


entry = 1 #input
out = []
i = 0

while True:
    opcode = program[i] % 100
    modes  = (program[i]//100%10, program[i]//1000%10, program[i]//10000%10)

    if   opcode == 99: break

    elif opcode == 1 or opcode == 2:
        a = program[i+1] if modes[0] else program[program[i+1]]
        b = program[i+2] if modes[1] else program[program[i+2]]
        program[program[i+3]] = a + b if opcode == 1 else a * b
        i += 4

    elif opcode == 3 or opcode == 4:
        a = program[i+1]
        if opcode == 3: program[a] = entry
        else:           out.append(program[a])
        i += 2

result = out[-1]
print("result", result)
submit(result)

