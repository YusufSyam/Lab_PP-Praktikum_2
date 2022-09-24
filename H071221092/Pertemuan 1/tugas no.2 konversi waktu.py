#Program Konversi Waktu

print ("konversi angka 140153 ke dalam jam : menit : detik")

jumlah = int(input("Masukkan angka diatas= "))
jam    = jumlah//3600 
jam1   = jumlah%3600
menit  = jam1//60
detik  = jam1%60

print (jam, ":", menit, ":", detik)