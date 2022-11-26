variabel_awal = 0
variabel_kedua = 1

n = int(input(" "))

print(variabel_awal, end=" ")
print(variabel_kedua, end=" ")

for i in range(n-2):
  variabel_baru=variabel_awal+variabel_kedua
  variabel_awal=variabel_kedua
  variabel_kedua=variabel_baru
  print(variabel_baru, end=" ")