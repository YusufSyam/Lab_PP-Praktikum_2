a = int(input("Nilai = "))

if a >= 90 :
    b = "'A'"
elif 90>a>=80 :
    b = "'B'"
elif 80>a>=70 :
    b = "'C'"
elif 70>a>=60 :
    b = "'D'"
elif 60>a>=40 :
    b = "'E'"
else :
    b = "'F'"

print("> nilai", a, "=", b)