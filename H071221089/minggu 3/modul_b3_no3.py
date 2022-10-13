
harga = int(input('harga barang : '))
bayar = int(input('uang yang dibayarkan : '))
kembalian = bayar - harga

dict_uang = {100000:"100.000", 50000:"50.000", 20000:"20.000", 10000:"10.000", 5000:"5.000", 2000:"2.000", 1000:"1.000"}
uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
for i in uang:
    if kembalian >= i:
        jumlah = kembalian // i
        kembalian = kembalian % i
        print(f'{jumlah} uang Rp. {dict_uang[i]}')
    else:
        print(f'0 uang Rp. {dict_uang[i]}')
