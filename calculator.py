import re

print("Calculator")
print("Type 'quit' to exit\n")

prev = 0
run = True

def performMath():
    global run
    global prev
    equation = ""
    if prev == 0:
        equation = input("Enter Equation: ")
    else:
        equation = input(str(prev))

    if equation == 'quit':
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if prev == 0:
            prev = eval(equation)
        else:
            prev = eval(str(prev) + equation)

while run:
    performMath()