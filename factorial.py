num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("sorry negative number doesnot have factorial ")
elif num == 0:
    print("Factorial of 0 is 1")
else:

    for i in range(1, num + 1):
        factorial = factorial*i
# if we indent print statement to be part of for loop it will print multiple statement till answer reaches Ye bhi loop ho ga sath sath
    print( "the factorial of", num, "is",factorial)
