def nor(n):
    # print(n)
    lenght = sum(list(map(lambda x:len(x),n)))
    if lenght % 2 != 0:
        print("BIG NO")
        return 
    for i in n:
        if i[0].upper() == "R":
            print("BIG NO")
            return
    print("BIG YES")
        

nor(input().split())
