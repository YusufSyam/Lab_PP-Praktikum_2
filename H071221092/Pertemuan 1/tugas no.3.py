#Program Menghitung Volume dan Luas Permukaan Kerucut

print("Jari-jari = r")
print("Tinggi    = t")
print("r = 18")
print("t = 21")

r = int(input("Masukkan Jari-jari: "))
t = int(input("Masukkan Tinggi: "))

phi = 3.1415926535898
s = (r*r)+(t*t)
s= s**0.5
        
Luas   = (phi*r*s)+phi*r*r
Volume = 1/3*(phi*r*r*t)

print(' {:.2f} m'.format(Luas))
print(' {:.2f} m'.format(Volume))
