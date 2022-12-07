def cap(n):
    for i in n:
        # print(i[0].upper())
        if i[0] != i[0].upper():
            print("No") 
            return
    print("Yes")

cap(input().split())