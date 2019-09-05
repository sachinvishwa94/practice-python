num = int(input('enter: '))
a = 1
print("rupee 1 on first day and then:")
for i in range(2,num+1):
    b = 2*a
    a = b
    print('day',i ,'=', b)