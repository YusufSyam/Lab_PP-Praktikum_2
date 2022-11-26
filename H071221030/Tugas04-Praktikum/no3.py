a = int(input())
b = input().split()
for i in range(len(b)):
    b[i]=int(b[i])
kecil = min(b)
urut = []

while len(b) > 0 :
    urut.append(kecil)
    b.remove(kecil)
    if len(b) > 0 :
        kecil = min(b)

print(urut)