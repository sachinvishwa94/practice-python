x = int(input("Enter a number to check whether its Prime or not: "))

for i in range(2, x):
    if x % i == 0:
        print("Not prime")
        break
else:
    print("You have evtered a prime number.")