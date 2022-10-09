n= int(input())

arr= input().split(' ')

for i in range(len(arr)):
    arr[i]= int(arr[i])

min_= min(arr)
sorted_arr= []

while len(arr)>0:
    sorted_arr.append(min_)
    arr.remove(min_)

    if len(arr)>0:
        min_= min(arr)

print(sorted_arr)