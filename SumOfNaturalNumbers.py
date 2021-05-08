# sum of squares of N natural numbers

num = int(input("Enter Natural Number :"))
sum = 0
for i in range(1,num+1):
    sum = sum + (i*i)

print("Sum of Squares Of natural numbers of ",num," is  ",sum)