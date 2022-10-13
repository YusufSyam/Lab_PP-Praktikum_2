a = int(input("Masukkan Bilangan : "))

def faktorial(n):
    jumlah = 1
    for i in range(1, n+1):
        jumlah*=i 
    return jumlah   

print(faktorial(a))