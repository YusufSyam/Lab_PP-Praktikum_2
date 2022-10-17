x = list(map(int, input("Masukkan Array 1: ").split()))
y = list(map(int, input("Masukkan Array 2: ").split())) ; n = []
for i in x:
    if i in y:
        if i not in n:
            n.append(i)
    

if len(n) == 0:
    print (f"tidak ada duplikat")
else:
    print(f"Terdapat {len(n)} buah duplikat yaitu {tuple((n))}")
