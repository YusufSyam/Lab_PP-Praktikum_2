def kelipatandua(n):
    arr = [2]
    for i in range(n-1):
        arr.append(arr[-1]*2)
    arr = map(str,arr)
    print(" ".join(arr))
    
kelipatandua(int(input()))