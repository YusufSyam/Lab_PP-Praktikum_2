nama = input().split(' ')
panjang = sum([len(nama[i]) for i in range(len(nama))])
[print('BIG NO') & exit() for i in range(len(nama)) if 'R' == nama[i][0].upper()]
print('BIG YES') if panjang % 2 == 0 else print('BIG NO')