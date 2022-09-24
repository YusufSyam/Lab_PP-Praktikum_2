import math

print('---semua inputan angka di bawah dinyatakan dalam satuan meter (m)---')
h= int(input('ketinggian menara : '))
a= int(input('sudut elevasi terhadap ujung depan kapal : '))
b= int(input('sudut elevasi terhadap ujung belakang kapal : '))

a1= math.radians(a)
a2= math.tan(a1)
a3= a2 * h

b1= math.radians(b)
b2= math.tan(b1)
b3= b2 * h 

hasil11= a3-b3
hasil12= round(hasil11, 1)
print('panjang kapal adalah : ', hasil12, 'm')