#menghitung panjang kapal
import math

h= int(input('h: '))

a = int(input('a: '))
rad = (math.pi/180)*a 
x = math.tan(rad)

b = int(input('b: '))
rad = (math.pi/180)*b 
y =math.tan(rad)

hasil = h * x - h * y
print('{:.1f} m'.format(hasil))