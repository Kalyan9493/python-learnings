# Fibonacci Sequence Up to given number

num = int(input("Enter Number : "))

prev = 0
next = 1
print(prev)
print(next)
for i in range(2,num+1):
    series = prev+next
    prev = next
    next = series
    if series > num:
        break

    print(series)