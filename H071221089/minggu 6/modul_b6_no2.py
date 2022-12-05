a = str(input()) ; a = a + ".txt"
b = str(input()) ; b = b + ".txt"

try :
    with open (a,"r") as origin :
        x = origin.read()
        x = x.split("\n")
        terpanjang = 0
        for i in x :
            if (len(i)>terpanjang):
                terpanjang = len(i)

except :
        print ("\nGagal")
else :
    with open (b,"w") as copy :
        for i in x :
            copy.write(" "*(terpanjang-len(i))+i+"\n")
        print(x)
        print("\nBerhasil")
