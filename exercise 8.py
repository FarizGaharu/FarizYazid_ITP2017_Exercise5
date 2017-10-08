import math
def a(x):
    return x**2
a=lambda x:x**2
print(a(1))


def b(y, i):
    return math.sqrt(y**2 + i**2)
b=lambda y, i: y**2+i**2
print(b(1,2))


def c(*args):
    return sum(args)/len(args)
c=lambda *args:sum(args)/len(args)
print(c(15,15,0))


def d(abcd):
    return "bcda"
d= lambda s:''.join(set(s))
print(d("silly"))
