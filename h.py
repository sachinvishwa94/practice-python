x = int(input())
y = int(input())
power = 1
for num in range(1,y+1):
    power = power*x
power = str(power)
print(power[-2:])