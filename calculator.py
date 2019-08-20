import re

print("MY FIRST EVER CALCULATAR")
print("Type quit to exit\n")

previous = 0
run = True


def my_math():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter Equation:")
    else:
        equation = input(str(previous))


    if equation == "quit":
        run = False
    else:
        equation = re.sub('[a-zA-Z,." ([]', '', equation)
        if previous ==0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


        print("output:", previous)


while run:
    my_math()
