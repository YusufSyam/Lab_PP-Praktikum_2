x = int(input('masukkan nilai x: '))
y = int(input('masukkan nilai y: '))

if x>0 and y>0:
    print((x, y), 'berada pada kuadran I')
elif x<0 and y>0:
    print((x, y), 'berada pada kuadran II')
elif x<0 and y<0:
    print((x, y), 'berada pada kuadran III')
elif x>0 and y<0:
    print((x, y), 'berada pada kuadran IV')
elif y==0 and x<0 or x>0:
    print((x, y), 'berada pada garis x')
elif x==0 and y<0 or y>0:
    print((x, y), 'berada pada garis y')
elif x==0 and y==0:
    print((x, y), 'berada pada titk pusat')
