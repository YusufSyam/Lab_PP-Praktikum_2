from turtle import Vec2D


n = int(input(" "))
v2 =0
v1 =1

for i in range(n):
    if i == 0:
        print(v2, end=' ')
    elif i == 1:
        print(v1, end=' ')
    else:
        v3 = v2 + v1
        v2 = v1
        v1 = v3
        print(v3, end=' ')
        

