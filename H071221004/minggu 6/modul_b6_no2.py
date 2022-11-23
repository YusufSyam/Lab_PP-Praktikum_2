
try:
    file1 = input('Masukkan nama file : ') + '.txt'
    file2 = input('Masukkan nama  salinan : ') + '.txt'

    fileasli = open(file1,'r')
    with open(file2,'w') as copy:
        panjang_string_terpanjang = 0
        fileasli2= []

        for i in fileasli:
            if len(i)>=panjang_string_terpanjang:
                panjang_string_terpanjang=len(i)
            fileasli2.append(i)

        for i in fileasli2:
            if i[len(i)-1] == '\n' :
                spasi = " "*(panjang_string_terpanjang-len(i))
            else:
                spasi = " "*(panjang_string_terpanjang-1-len(i))
            copy.write(spasi + i)
    print('\nBerhasil')
except:
    print('\nGagal')

fileasli.close()
