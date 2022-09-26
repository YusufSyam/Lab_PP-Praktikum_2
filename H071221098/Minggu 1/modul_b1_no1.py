#Menghitung panjang kapal
import math
from re import A

h = int(input('h: '))


a = int(input('a: '))
rad = (math.pi/180)*a
x =math.tan(rad)
#x = float(hasilTan1)

b = int(input('b: '))
rad = (math.pi/180)*b
y =math.tan(rad)
# y = float(hasilTan2)

hasil = round(h * x - h * y,1)
print(hasil,'m')

