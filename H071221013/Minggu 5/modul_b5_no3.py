x = set(map(int, input('Input array Ke 1: ').split()))
y = set(map(int, input('Input array Ke 2: ').split()))

#duplikat = tuple(x & y)
#print(f'Terdapat {len(duplikat)} buah duplikat yaitu {duplikat}');
a = x.intersection(y)

if len(a)==0:
    print("Tidak ada duplikasi")
else:
    print(f"Terdapat {len(a)} buah duplikat yaitu", tuple(a))




