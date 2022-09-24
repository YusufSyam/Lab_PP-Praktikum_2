nilai = int(input('nilai :'))

if nilai >= 90 : index = 'A'
elif nilai >= 80 : index = 'B'
elif nilai >= 70 : index = 'C'
elif nilai >= 60 : index = 'D'
elif nilai >= 40 : index = 'E'
elif nilai < 40 : index = 'F'
print (f'> nilai {nilai} = {index}')