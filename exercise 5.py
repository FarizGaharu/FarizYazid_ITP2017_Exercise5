w = int(input('input first number here: '))
x = int(input('input second number here: '))
y = str(input('+,-,*,/' + '\nInput the funtion from the choice above: ')).lower()
z = str(input('float/ int' + '\nInput the output format: ')).lower()
def calculator(w,x,y,z):
    if y == "+":
        result = w + x
    elif y == "-":
        result = w - x
    elif y == "*":
        result = w * x
    elif y == "/":
        result = float(w/x)

    if z == "int":
        return print(round(int(result)))
    elif z == 'float':
        return print(float(result))

calculator(w,x,y,z)
