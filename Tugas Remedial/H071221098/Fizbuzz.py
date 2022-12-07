a = int(input())
if a % 15 == 0:
    print('fizbuzz')
elif a % 3 == 0:
    print('fiz')
elif a % 5 == 0:
    print('buzz')
else:
    print('-')