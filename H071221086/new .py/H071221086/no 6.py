def fpb (a,b,c):
    if (c == 0):
        return a
    elif (c > 0):
        return fpb(c, a % b % c)

fpb
a = input('masukkan angka pertama : ')
b = input('masukkan angka kedua: ')
c = input('masukkan angka ketiga: ')

input_numerik = a.isnumeric() and b.isnumeric() and c.isnumeric()
if(input_numerik):
    a= int(a)
    b= int(b)
    c= int(c)
    print('FPB dari', a,b,c,': ', fpb(a,b,c))