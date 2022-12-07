a = int(input('masukkan data: '))
b = int(input('masukkan data: '))

if a < b:
    for i in range(1, b+1):
        print(i ,end = '\n' if i % a == 0 else ' ')
else:
    print('invalid')