bil = (input().split())
x = int(bil[0])
y = int(bil[1])
angka1 = x
angka2 = y
while x != y:
    if x>y: 
        y = angka2 + y
    else:
        x = angka1 + x