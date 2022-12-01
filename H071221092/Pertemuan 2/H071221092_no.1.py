nilai = (input("Masukkan nilai angka: "))
nilai = eval (nilai)
if nilai >= 90:
   na = "'A'"
elif nilai >= 80:
   na = "'B'"
elif nilai >= 70:
   na = "'C'"
elif nilai >= 60:
   na = "'D'"
elif nilai >= 40:
   na = "'E'"
elif nilai < 40:
   na = "'F'"

print ("nilai", nilai, "=",na)