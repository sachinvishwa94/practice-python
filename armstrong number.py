num = int(input("Enter a Number: "))
sum = 0
a = num
digit_lenght = len(str(num))
while num > 0:
    digit = num % 10
    sum = sum  + digit ** digit_lenght
    num = num // 10
if a == sum:
    print(sum,"is an ARMSTRONG NUMBER")
else:
    print(sum,"This is not an ARMSTRONG NUMBER")