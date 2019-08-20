
fibo_cache = {}

def fib(n):

    a = 0
    b = 1

    if n == 1:
        print(a)

    elif n < 0:
        print("Invalid input")

    else:
        print(a)
        print(b)
        for i in range(2,n):

            c = a + b
            a = b
            b = c
            #if we want to print number in this series which has value less than hundred use if statement

            print(i, ";", c)
            print(a)



fib(50000)