#// TEST TO ADD THE STEP FUNCAO, STILL IN DEVELOPMENT.

user= 1
step = 3
immutablestep = step+1
l =range(1, 30)

for chr in l:
    if l.index(chr) == step:
        print("step... {}".format(chr))
        step = step+immutablestep
    else:
        print(chr)
    
print(immutablestep)