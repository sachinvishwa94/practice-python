import math

num = int(input("Enter a number: "))

root = math.sqrt(num)
if int(root + 0.5)**2 == num:
    print("perfect square ")
else:
    print("not a perfect square")

