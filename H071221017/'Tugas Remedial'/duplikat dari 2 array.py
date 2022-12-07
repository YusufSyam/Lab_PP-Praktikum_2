def duplikat(arr1,arr2):
    if len(arr1) != len(arr2):
        print("inputan tidak valid")
        return
    for i in range(len(arr1)):
        if arr1[i] in arr2 or arr2[i] in arr1:
            print("terdapat duplikat")
            break
        else: 
            print("tidak terdapat duplikat")
            break

n1 = list(map(int,input().split()))
n2 = list(map(int,input().split()))
duplikat(n1,n2)