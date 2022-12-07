x = int(input())
arr = list(map(int, input().split()))
arr = arr[x:] + arr[:x]

for i in arr:
    arr = int(i)
    print(arr, end=' ')