def jabat(n):
    if n <= 0:
        print("0")
        return 
    jabat = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            if j != i:
                jabat+=1
    print(jabat)
    
jabat(int(input()))