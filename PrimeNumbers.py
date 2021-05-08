# Print all Prime numbers in between an interval

startNum = int(input("Enter the First Number : "))
lastNum = int(input("Enter the Last Number : "))

def printPrimeNumbers(first,last):
    for i in range(first,last+1):
        count = 0
        for j in range(1,i+1):
            if i%j == 0:
                count+=1
        if count == 2:
            print(i)

printPrimeNumbers(startNum,lastNum)