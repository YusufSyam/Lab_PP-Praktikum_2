
h = int(input('nilai h :'))
a = int(input('nilai a :'))
b = int(input('nilai b :'))

import math 
panjang_keseluruhan = math.tan(a*(math.pi/180))*h
panjang_sisa = math.tan(b*(math.pi/180))*h
print('{:.1f} m'.format(panjang_keseluruhan-panjang_sisa))
