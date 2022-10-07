nilai = int(input("Nilai = "))

if nilai >=90:
    Total_nilai = ("'A'")
elif nilai >=80:
    Total_nilai = ("'B'")
elif nilai >=70:
    Total_nilai = ("'C'")
elif nilai >=60:
    Total_nilai = ("'D'")
elif nilai >=40:
    Total_nilai = ("'E'")
elif nilai <40:
    Total_nilai = ("'F'")

print('> nilai', nilai,'=',Total_nilai)
