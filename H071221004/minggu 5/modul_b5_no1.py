mat1 = []
mat2 = []

def matriks1():
    for baris in range(2):
        mat_baris = []
        for kolom in range(2):
            elemen_baru = int(input(f'Input nilai matriks pertama index {baris+1},{kolom+1} :'))
            mat_baris.append(elemen_baru)
        mat1.append(mat_baris)
    return mat1
    
def matriks2():
    for baris in range(2):
        mat_baris = []
        for kolom in range(2):
            elemen_baru = int(input(f'Input nilai matriks kedua index {baris+1},{kolom+1} :'))
            mat_baris.append(elemen_baru)
        mat2.append(mat_baris)
    return mat2


result = [[0,0],
[0,0]]

def hasilkali():
    result[0][0] = (mat1[0][0] * mat2[0][0]) + (mat1[0][1] * mat2[1][0])
    result[0][1] = (mat1[0][0] * mat2[0][1]) + (mat1[0][1] * mat2[1][1])
    result[1][0] = (mat1[1][0] * mat2[0][0]) + (mat1[1][1] * mat2[1][0])
    result[1][1] = (mat1[1][0] * mat2[0][1]) + (mat1[1][1] * mat2[1][1])
    
    print(' |',  (mat1[0][0]),(mat1[0][1]), '|', 'x', '|', (mat2[0][0]),(mat2[0][1]), '|', '=', '|', (result[0][0]),(result[0][1]), '|')
    print(' |',  (mat1[1][0]),(mat1[1][1]), '|', ' ', '|', (mat2[1][0]),(mat2[1][1]), '|', ' ', '|', (result[1][0]),(result[1][1]), '|')
    return result



matriks1()
matriks2()


hasil_kali=hasilkali()
print(hasil_kali)