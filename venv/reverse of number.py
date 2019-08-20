num = int(input("Enter a number: "))

rev = 0

while num > 0:

    dgt = num % 10
    rev = rev*10 + dgt
    num = num//10

print("rev of the number is:", rev)

'''''
logic here is that if a number is first divided by 10,
then remainder left will be become first number of reversed value in first attempt, 
and there after we multiply the previous remainder by 10 and add to new remainder and on completion of this we get our
reversed number

'''''