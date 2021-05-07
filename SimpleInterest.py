# Simple interest program

principalAmount = int(input("Enter Principle Amount : "))
time = int(input("Enter Time in months : "))
rate = float(input("Enter Interest Rate : "))

def simpleInterest(p,t,r):
    return (p*t*r)/100

SI = simpleInterest(principalAmount,time,rate)
print("Interest Rate is : ",SI)

print("Total Amount is : ",principalAmount + SI)