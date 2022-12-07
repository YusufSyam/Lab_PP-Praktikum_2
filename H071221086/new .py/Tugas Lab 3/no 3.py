harga_barang = int(input('harga barang: '))
uang_pembeli = int(input('uang pembeli: '))
kembalian = uang_pembeli - harga_barang
uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
if harga_barang < uang_pembeli:
    for i in uang:
        c = kembalian // i
        print('%d uang RP. %d '% (c, i))
        kembalian -= c*i
elif harga_barang == uang_pembeli:
    print('0')
else:
    print('inputan uang pembeli harus lebih besar dari pada harga barang')
