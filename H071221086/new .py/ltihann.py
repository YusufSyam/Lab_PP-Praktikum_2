#mengganti/mengghapus karakter di dalam string misal: "Halo" -> "Hao"
a = input()
target = input()
pilih = int(input('Pilih : '))
if pilih == 1:
    ganti = input()
    a = a.replace(target, ganti)
elif pilih == 2:
    a = a.replace(target, '')
print(a)