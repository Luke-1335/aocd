from aocd import data, submit
words = data.split("\n")


for w1 in words:
    for w2 in words:
        diff, pos = 0, 0
        
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff +=1
                if diff == 2: break
                pos = i
                
        if diff == 1:
            result = w1[:pos] + w1[pos+1:]
            print("result", result)
            submit(result)
            exit()

