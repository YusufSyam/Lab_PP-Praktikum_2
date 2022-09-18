print('\nMenghitung panjang kapal')

h= float(input('\nMasukkan tinggi menara : '))
a = int(input('Sudut elevasi pengamat terhadap ujung belakang kapal : '))
b= int(input('Sudut elevasi pengamat terhadap ujung depan kapal : '))


import math
rad= (math.pi/180)*a
tan_a= math.tan(rad)

rad= (math.pi/180)*b
tan_b= math.tan(rad)

ac= tan_a*h
bc= tan_b*h

ab = float(ac-bc)
print('{:.1f} m'.format(ab))
