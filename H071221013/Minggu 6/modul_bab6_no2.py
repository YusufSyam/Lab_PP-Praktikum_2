file1 = input("Masukkan nama file : ")
file2 = input("Masukkan nama file : ")

# try:
with open(file1 + ".txt", "r") as file1:
    data = file1.read()
    print(data)

    data = data.split("\n")
    data[-1] = data[-1]+"\n"
    print(data)
    x = 0
    for i in data:
        if len(i) > x:
            x = len(i)

with open(file2 + ".txt", "w") as file2:
    for i in data:
        file2.write(" " * (x- len(i)) + i + "\n")

print("Berhasil")
