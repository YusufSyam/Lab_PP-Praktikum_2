x = int(input(''))
def factorial(x):
    if x < 0:
        return('tak terdefinisi')
    elif x == 0:
        return 1
    else:
        return ( x * factorial(x-1))
print(factorial(x))