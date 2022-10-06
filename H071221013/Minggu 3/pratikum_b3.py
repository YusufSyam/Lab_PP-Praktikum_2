t = int(input("Masukkan Tinggi Segitiga: "))
for i in range(1, t+1):
    print((t-i) * "  " + (i * "* ") + ((i-1) * "* "))
    
