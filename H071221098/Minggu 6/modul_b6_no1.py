f = (input(""))
n = (input(""))
try:
    with open(f+".txt","r") as latihan:
        file = latihan.read()
    with open(n+".txt", "w") as copy:
        copy.write(file)
        print("berhasil")
except :
    print("gagal")