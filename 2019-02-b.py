from aocd import data, submit
lines = data.split("\n")


for noun in range (99):
    for verb in range (99):
        program = [int(val) for line in lines for val in line.split(",")]
        program[1] = noun
        program[2] = verb

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

        if 19690720 == program[0]:
            result = 100 * noun + verb
            print("result", result)  
            submit(result)
            exit()

