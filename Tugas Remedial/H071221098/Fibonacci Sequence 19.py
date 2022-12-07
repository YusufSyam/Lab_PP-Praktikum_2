bil = int(input())
n1, n2 = 0, 1
count = 0

if bil <= 0:
    print(0)
elif bil == 1:
   print(n1)
else:
   while count < bil:
       print(n1, end=' ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1