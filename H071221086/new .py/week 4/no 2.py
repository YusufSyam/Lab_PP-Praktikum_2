def hitung_FPB(x,y):
    if (y==0):
        return x
    else:
        return hitung_FPB(y,x%y)

x = int(input(' '))
y = int(input(' '))
print(f'FPB dari {x} dan {y} = {hitung_FPB (x,y)}')
    