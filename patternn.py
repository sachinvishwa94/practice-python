av = 10

x = int(input("how many dosas you want ?"))

i = 1

while i <= x:

    if i > av:
        print('Out of stock')
        break
    print("DOSA")
    i += 1

