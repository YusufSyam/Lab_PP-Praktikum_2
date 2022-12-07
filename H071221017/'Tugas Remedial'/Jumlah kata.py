def kata(n):
    n = n.lower()
    n = n.split()
    n.sort()
    dic = dict()
    for i in n:
        dic[i] = n.count(i)
    for i,v in dic.items():
        print(f'{i}, {v}')

kata(input())