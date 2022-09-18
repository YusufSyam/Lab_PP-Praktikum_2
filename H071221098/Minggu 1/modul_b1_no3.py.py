seller = input("Nama seller: ")
gaji_pokok = int(input("Gaji pokok: "))
total_penjualan = int(input("Total penjualan: "))

total = 15/100 * total_penjualan + gaji_pokok
total = "{:.2f}".format(total)

print("Total gaji", seller, "= $" + str(total))