arr = []
array_1 = input("Input array ke 1: ").split()
array_2 = input("Input array ke 2: ").split()
arr = array_1 + array_2

dup = []
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            dup.append(arr[i])
dup = set(dup)
print(f"Terdapat {len(dup)} buah duplikat yaitu {dup}")