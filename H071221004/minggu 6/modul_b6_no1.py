file1 = input("Masukkan nama file : ") + '.txt'
file2= input("Masukkan nama salinan : ") + '.txt'

try: 
    with open(file1, "r") as fileasli:
        tampilkan = fileasli.read()
except:
    print('\nGagal')

else:    
    with open(file2, 'w') as copy:
        copy.write(tampilkan)
    print('\nBerhasil')