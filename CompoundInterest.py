# Compound Interest

principalAmount = int(input("Enter Principle Amount : "))
time = int(input("Enter Time in months : "))
rate = float(input("Enter Interest Rate : "))

def compoundInterest(p,t,r):
    return p * ((1 + (r/100)) ** t)

amount = compoundInterest(principalAmount,time,rate)
CI = amount - principalAmount
print("Compound Interest Rate is : ",CI)

print("Total Amount is : ",principalAmount + CI)