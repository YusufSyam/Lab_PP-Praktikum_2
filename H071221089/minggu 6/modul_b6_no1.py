a = str(input()) ; a = a + ".txt"
b = str(input()) ; b = b + ".txt"

try :
    with open (a,"r") as origin :
        x = origin.read()
except :
        print ("\nGagal")
else :
    with open (b,"w") as copy :
        copy.write(x)
        print("\nBerhasil")
