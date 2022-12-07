d = int(input())
arr = list(map(int, input().split()))
arr = arr[d:] + arr[:d]

for i in arr:
    arr = int(i)
    print(arr, end=' ')