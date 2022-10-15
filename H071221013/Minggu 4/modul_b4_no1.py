panjang= int(input())
m= input().split(' ')

if panjang!=(len(m)):
    print("Panjang Tidak Sesuai")
else:
    for i in range(len(m)):
        m[i]= int(m[i])

    sorted_m= []

    while len(m)>0:
        minimum= min(m)
        sorted_m.append(minimum)
        m.remove(minimum)

    print(sorted_m)