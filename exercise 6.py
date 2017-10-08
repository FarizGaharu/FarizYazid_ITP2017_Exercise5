import math
w = int(input('input first number here: '))
x = int(input('input second number here: '))
y = str(input('+,-,*,/' + '\nInput the funtion from the choice above: ')).lower()
z = str(input('float/ int' + '\nInput the output format: ')).lower()
def calculator( opr="+", out="float",*num):
    if not num:
        raise ValueError("please enter a number")
    res=num[0]
def calculator(w,x,y,z):
    if y == "+":
        result = w + x
    elif y == "-":
        result = w - x
    elif y == "*":
        result = w * x
    elif y == "/":
        result = float(w/x)
    else:
        raise ValueError

    if z == "int":
        return print(round(int(result)))
    elif z == 'float':
        return print(float(result))
    else:
        raise ValueError
    return result
    print("please print the data accurately!")
calculator(w,x,y,z)
