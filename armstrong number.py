num = int(input("Enter a Number: "))
sum = 0
a = num
while num > 0:
    digit = num % 10
    sum = sum+ digit*digit*digit
    num = num// 10
if a == sum:
    print("This number is an ARMSTRONG NUMBER")
else:
    print("THis is not an ARMSTRONG NUMBER")