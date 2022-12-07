x = int(input('N: '))

a=0
b=1

for i in range(x):
    print(a , end= ' ')
    c = a + b
    a = b
    b = c