print("==================================================")
print("   Program Konversi Dari Detik ke Jam Dan Menit   ")
print("==================================================")


    # menampilkan informasi program
print("Konversi Detik ke Jam dan menit\n")

# input total detik
totaldetik = int(input('Masukkan Detik \t: '))

# melakukan konversi hh:mm:ss ke detik
hh = totaldetik // 3600
sisadetik = totaldetik % 3600
mm = sisadetik // 60
ss = sisadetik % 60

# menampilkan hasil konversi
print("{} detik sama dengan {} : {} : {}".format(totaldetik, hh, mm, ss))

    

