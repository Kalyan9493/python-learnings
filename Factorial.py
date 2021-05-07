# Factorial of given number  using For Loop
print("===================  Using For Loop ====================================")
number = int(input("Enter Number : "))
result = 1
for i in range(1,number+1):
    if number > 1 :
        result = result * i
    elif number == 0 :
        print("Factorial of ",number, " is 1")
    else :
        print("Invalid input")

if number > 1:
    print("Factorial of ",number," is ",result)



# Factorial of given number  using For Recursion

print("===================  Using Recursion ====================================")
def factorial(num):
    if num >= 0 :
        return 1 if (num == 0 or num == 1)  else num * factorial(num-1);
    else:
        return 0

print("Factorial of ",number," is ",factorial(number))


# Factorial Using in-built function
print("===================  Using In-Built Function====================================")
import  math
if number >= 0:
    print("Factorial of ",number, " is ",math.factorial(number))
else:
    print("Invalid Input")