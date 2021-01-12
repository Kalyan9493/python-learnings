# Print Pattern
#APQR 
#ABQR
#ABCR
#ABCD

str1 = "ABCD"
str2 = "PQRS"

for i in range(len(str1)):
    for  j in range(i):
        print(str1[j], end="")
    print()