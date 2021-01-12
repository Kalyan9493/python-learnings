#1234
#234
#34
#4

for i in range(4):
    for j in range(4-i):
        print(j+i+1," ",end="")
    print()