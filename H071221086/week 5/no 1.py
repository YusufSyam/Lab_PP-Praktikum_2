matriks1 = []
for i in range (2):
    baris = []
    for j in range (2):
        angka = int(input(f'input nilai matriks pertama index {i+1}, {j+1}: '))
        baris.append(angka)
    matriks1.append(baris)

matriks2 = []
for i in range (2):
    baris = []
    for j in range (2):
        angka = int(input(f'input nilai matriks kedua index {i+1},{j+1}: '))
        baris.append(angka)
    matriks2.append(baris)
c = matriks1[0][0]*matriks2[0][0] + matriks1[0][1]* matriks2[1][0]
d = matriks1[0][0]*matriks2[0][1] + matriks1[0][1]* matriks2[1][1]
e = matriks1[1][0]*matriks2[0][0] + matriks1[1][1]* matriks2[1][0]
f = matriks1[1][0]*matriks2[0][1] + matriks1[1][1]* matriks2[1][1]
print(f'| {matriks1 [0][0]}, {matriks1 [0][1]} | x | {matriks2[0][0]}, {matriks2[0][1]} | = | {c}. {d} |')
print(f'| {matriks1 [1][0]}, {matriks1 [1][1]} | x | {matriks2[1][0]}, {matriks2[1][1]} | = | {e}. {f} |')