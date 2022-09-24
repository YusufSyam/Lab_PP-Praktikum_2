a = int(input('A ='))
b = int(input('B ='))
c = int(input('C ='))
if a>=b and a>=c :
    nilai = a
elif b>=c and b>=a :
    nilai = b
elif c>=a and c>=a :
    nilai = c
else :
    print ('data tidak valid')
print (f'{nilai} adalah nilai terbesar')




