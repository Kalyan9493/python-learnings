# find given number is armstrong or not

num = input("Enter number : ")
count = len(num)

def isArmstrong(num,count):
    result = 0
    for i in range(0,count):
        result = result + (int(num[i]) ** count)
    if(int(num) == result):
        return True
    return False
try:

    if isArmstrong(num,count):
        print("Given ", num, "is Armstrong Number")
    else:
        print("Given ", num, "is Not an Armstrong Number")
except ValueError as e:
    print("Invalid Input")
except Exception as e:
    print("Something Went Wrong")