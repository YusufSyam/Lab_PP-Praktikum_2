matriks1 = [[int(input("Input Nilai Matriks Pertama Index {},{} : ". format (baris, kolom))) for kolom in range (1, 2+1)] for baris in range (1, 2+1)]
matriks2 = [[int(input("Input Nilai Matriks Kedua Index {},{} : ". format (baris, kolom))) for kolom in range (1, 2+1)] for baris in range (1, 2+1)]
hasil = [[0,0], [0,0]]

def hasil_kali() :
    hasil[0][0] = (matriks1[0][0]*matriks2[0][0]) + (matriks1[0][1]*matriks2[1][0])
    hasil[0][1] = (matriks1[0][0]*matriks2[0][1]) + (matriks1[0][1]*matriks2[1][1])
    hasil[1][0] = (matriks1[1][0]*matriks2[0][0]) + (matriks1[1][1]*matriks2[1][0])
    hasil[1][1] = (matriks1[1][0]*matriks2[0][1]) + (matriks1[1][1]*matriks2[1][1])
    print ('Hasil Perkalian Matriks')
    print("| {}, {} | x | {}, {} | = | {}, {} |". format(matriks1[0][0], matriks1[0][1], matriks2[0][0], matriks2[0][1], hasil[0][0], hasil[0][1]))
    print("| {}, {} |   | {}, {} |   | {}, {} |". format(matriks1[1][0], matriks1[1][1], matriks2[1][0], matriks2[1][1], hasil[1][0], hasil[1][1]))
    return hasil
hasil_kali=hasil_kali()
print(hasil_kali)