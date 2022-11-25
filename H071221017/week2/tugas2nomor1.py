a, b, c = int(input("A : ")),int(input("B : ")),int(input("C : "))
if a < b and c < b:
    print("%d adalah nilai terbesar" % (b))
elif a < c and b < c: 
    print("%d adalah nilai terbesar" % (c))
else:
    print("%d adalah nilai terbesar" % (a))    
