x = int(input('Masukkan Bilangan Pertama : '))
y = int(input('Masukkan Bilangan Kedua: '))

def getFPB(x,y):
    if (y == 0):
        return x
    else:
        return getFPB(y, x % y)

def get_fpb_pemula(x, y):
    if x>y:
        smaller= y
    else:
        smaller= x

    fpb= 1
    for i in range(1,smaller+1):
        if x%i==0 and y%i==0:
            fpb= i

    return fpb


print(f'FPB dari {x} dan {y} =',get_fpb_pemula(x,y))

