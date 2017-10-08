def generator (x):
    b = -1
    while x > b:
        yield x
        x -= 1
countdown= generator(int(input("Input the number: ")))
for y in countdown:
    print(y)
print(type(countdown))
