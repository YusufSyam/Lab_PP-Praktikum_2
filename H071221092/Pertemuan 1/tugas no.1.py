#Menghitung Panjang Kapal
import math
from re import A

h   = int(input("h: "))

a   = int(input("a: "))
rad = (math.pi/180)*a
x   = math.tan(rad)

b   = int(input("b: "))
rad = (math.pi/180)*b
y   = math.tan(rad)

hasil = round(h*x-h*y,1)
print(hasil,"m")