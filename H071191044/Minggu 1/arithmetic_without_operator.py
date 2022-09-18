def add(x, y):
    if(x==y):
        return x*2

    bigger, smaller= max(x, y), min(x, y)
    total= (bigger*2) - (bigger-smaller)

    return total

def substract(x, y):
    # Todo
    pass

print(add(7,4))