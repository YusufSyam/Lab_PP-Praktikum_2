print('====program mencari volume dan luas permukaan kerucut====')

jari_jari_alas = int(input('Masukkan Jari-jari : '))
tinggi = int(input('Masukkan Tinggi : '))

r=jari_jari_alas
t=tinggi

phi = 3.1415926535898
s = (r*r)+(t*t)
S = s**0.5

volume = (phi*r*r*t)/3
luas_permukaan = (phi*r*S)+phi*r*r

print('{:.2f} m'.format(volume))
print('{:.2f} m'.format(luas_permukaan))