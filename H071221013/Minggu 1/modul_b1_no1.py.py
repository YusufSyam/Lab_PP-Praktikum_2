print("=====================================")
print("       Menghitung Panjang Kapal      ")
print("=====================================")


h = int(input("Masukkan Tinggi Menara :"))
a = int(input("Masukkan Sudut Elevasi Pengamat Terhadap Ujung Belakang Kapal :"))
b = int(input("Masukkan Sudut Elevasi Pengamat Terhadap Ujung Depan Kapal :"))

import math
psel = math.tan(a*math.pi/180)*h
psisa = math.tan(b*math.pi/180)*h
pk = psel - psisa
print("Panjang Kapal {:.1f}".format(pk))



