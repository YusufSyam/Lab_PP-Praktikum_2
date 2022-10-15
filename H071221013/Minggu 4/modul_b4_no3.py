n = input()

for i in range(1, len(n)+1):
    if i==len(n):
        print(n[len(n)-i:0:-1]+n[:i])
    else:
        print(n[len(n)-i:0:-1]+n[:i],end='|')