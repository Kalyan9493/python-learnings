# Find Area Of Circle

radius = float(input("Enter Radius : "))

def areaOfCircle(r):
    PI = 3.142
    return  PI * (r ** 2)

print("Area of Circle for given Radius is : %.4f"%areaOfCircle(radius))