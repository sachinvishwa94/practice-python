import math


def func(n):
    for i in range(1,n):
        sum = 0
        number = i
        x = 0
        rem = 0
        number= i
        x = int(math.log10(number) + 1)

        while number>0:

            rem = number % 10
            sum = sum + pow(rem, x)
            number = number // 10

        if i == sum:
            print(sum)

func(10000)