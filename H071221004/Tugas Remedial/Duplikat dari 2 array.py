x = list(map(int, input().split()))
y = list(map(int, input().split()))
z = 0

if len(x) == len(y):
    for i in x:
        for j in y:
            if i == j:
                z = z+1
    if z == 0:
        print('tidak terdapat duplikat')
        
    else:
        print('terdapat duplikat')
        
else:
    print('inputan tidak valid')
                
    