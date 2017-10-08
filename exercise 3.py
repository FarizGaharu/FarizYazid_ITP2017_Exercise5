from math import sqrt
x = (int(input()))
y = (int(input()))
def hypotenuse(a,b):
    try:
        return sqrt(a**2+b**2)
    except TypeError:
        return None

product = hypotenuse(2,3)
print(product)
product = hypotenuse("2,3")
print(product)
product = hypotenuse(2,'3')
print(product)

