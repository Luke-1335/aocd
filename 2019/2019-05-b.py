from numpy import prod
from aocd import data, submit
program = [int(d) for d in data.split(",")]


get_args = lambda i, modes, prog: [prog[i+n] if modes[n] else prog[prog[i+n]] for n in (1,2)] #return 2 arguments

entry = 5 #input
out = []
i = 0

while True:
    opcode = program[i] % 100
    modes  = (0, program[i]//100%10, program[i]//1000%10) #dummy zero for nice indexing in lambda get_args => modes[n] insted of modes[n-1]

    if opcode == 99: break

    elif opcode == 1 or opcode == 2:
        args = get_args(i, modes, program)
        program[program[i+3]] = sum(args) if opcode == 1 else prod(args)
        i += 4

    elif opcode == 3 or opcode == 4:
        arg = program[i+1]
        if opcode == 3: program[arg] = entry
        else: out.append(program[arg])
        i += 2

    elif opcode == 5 or opcode == 6:
        args = get_args(i, modes, program)
        if opcode == 6: args[0] = not args[0]
        i = args[1] if args[0] else i+3

    elif opcode == 7 or opcode == 8:
        args = get_args(i, modes, program)
        program[program[i+3]] = args[0] < args[1] if opcode == 7 else args[0] == args[1]
        i += 4

result = out[0]
print("result", result)
submit(result)

