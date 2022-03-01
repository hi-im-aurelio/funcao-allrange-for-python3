#// TEST TO ADD THE STEP FUNCAO, STILL IN DEVELOPMENT.

step = 0
immutablestep = step+1
l =range(1, 10)


for chr in l:
    if l.index(chr) == step:
        print("step... {}".format(chr))
        step = step+immutablestep
    else:
        print(chr)
    
print("Foram {} steps".format(immutablestep))