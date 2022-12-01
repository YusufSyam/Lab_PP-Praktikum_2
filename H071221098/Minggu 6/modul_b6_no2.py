f = (input(""))
n = (input(""))
try:
    with open(f+".txt","r") as latihan:
        file = latihan.read()
        x = latihan.read()
        x = x.split('\n')
        terpanjang = 0
        for i in x:
            if (len(i)>terpanjang):
                terpanjang = len(i)

    with open(n+".txt", "w") as copy:
        copy.write(file)
        print(x)
        print("berhasil")
except :
    print("gagal")