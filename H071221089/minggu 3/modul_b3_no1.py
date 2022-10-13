x = int(input("masukkan X= "))
y = int(input("masukkan Y= "))
i = 0 
while x > y:
    print("ingat y harus lebih besar dari x, harap ulangin masukan.")
    x = int(input("masukkan X= "))
    y = int(input("masukkan Y= "))
while i <= y-1: 
    print(i+1,end=" ")
    i += 1
    if ((i%x)==0):
        print()