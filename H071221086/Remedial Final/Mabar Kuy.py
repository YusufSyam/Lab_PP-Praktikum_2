a = int(input())
b = int(input())
c = int(input())
hasil = a + b + c
if hasil >= 81:
    komen = 'WP'
elif hasil >= 41 and hasil <= 80:
    komen = 'N1'
elif hasil >= 0 and hasil <= 40:
    komen = 'MB'

if a > b and a > c:
    mvp = 'Henokh'
elif b > a and b > c:
    mvp = 'Fikry'
elif c > b and c > a:
    mvp = 'Aditya'
    
print(f'MVP : {mvp}')
print(komen)