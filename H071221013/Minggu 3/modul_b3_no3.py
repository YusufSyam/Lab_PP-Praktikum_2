x = int(input("Harga Barang:Rp.  "))
y = int(input("Nilai Uang:Rp.  "))
z = y-x

n = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

for i in n:
    pembagian_kembalian = z//i
    print(f"{int(pembagian_kembalian)} uang Rp. {i}")
    z = z - (pembagian_kembalian*i)