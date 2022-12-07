x = int(input('masukkan x: '))
if x>0:
    for x in reversed(range(0, x)):
        x+= 1
        print('akar kuadrat dari:',x,':',x**0.5)
elif x<0:
    for x in range(x , 2):
        print('akar kuadrat dari:',x,':',x**0.5)

        