if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        print(i ** 2)

#soal kendaraan berpapasan
a = list(map(int, input().split()))
b = a[0]+a[1]
c = a[2]+a[3]
while b!=c:
    b+=a[1]
    c+=a[3]
    if b>99999999 or c>99999999999999999999999:
        print('TIDAK')
        break
if b==c:
        print('YA')

#soal kaos kaki
def zatzet(n, ar):
    num = 0 
    for i in range(0, n):
        gum = 1
        for j in range(i+1, n):
            if ar[i] == None:
                continue
            if ar[i] == ar[j] and gum == 1:
                num += 1
                gum += 1
                ar[j] = None
    return num
n = int(input())
ar = list(map(int, input().split()))
print(zatzet(n, ar))

#jarak minimum
q = int(input())
a = list(map(int, input().split(' ')))
target = 0
duplicate = False
length_duplicate = []
for i in range(len(a)) :
    target = i
    for j in range(i+1, len(a)) :
        if a[target] == a[j] :
            duplicate = True
            x = j-target
            length_duplicate.append(x)
length_duplicate.sort()


if duplicate == True:
    print(length_duplicate[0])
elif duplicate == False:
    print(-1)


#soal order bolak balik
b = int(input())
n = list(map(int, input().split(' ')))
if n[-1] == 0:
    n.pop(-1)
    for i in range (len(n)):
        for j in range (len(n)):
            if n[i] > n[j]:
                n[i],n[j] = n[j], n[i]
if n[-1] == 1:
    n.pop(-1)
    for i in range (len(n)):
        for j in range (len(n)):
            if n[i] < n[j]:
                n[i],n[j] = n[j], n[i]
for i in n:
    print(i, end=" ")



#soal batik
batik = input().split()
turunan = int(batik[0])
perantara = str(batik[1])
silangan = str(batik[2])
for i in range(turunan):
    for j in range(turunan):
        if i == j or i + j == turunan - 1:
            print(silangan, end="")
        else:
            print(perantara, end="")
    print()


#soal awan
input()
clouds = list(map(int,input().split()))
i = 0
totalstep = 0

while i < len(clouds)-1:
    if i + 2 < len (clouds)-1 and clouds[i+2]==1:
        i += 1
    else:
        i += 2
    
    totalstep += 1

print(totalstep)

#soal bintang bintang
n = int(input())

for i in range (n, 0, -1):
    print(("*"*i)+(" "*(n-i)*2)+("*"*i))