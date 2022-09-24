golongan = (input('golongan :')).upper()
daya = int(input('daya :'))
pemakaian = int(input('pemakaian :'))
if golongan == 'R1' :
    if daya == 900 :
        tagihan = (pemakaian*1352)
    elif  daya == 1300 :
        tagihan = (pemakaian*1444.70)
    elif  daya == 2200 :
        tagihan = (pemakaian*1444.70)
    else :
        print ('data tidak valid')
if golongan == 'R2' :
    if daya >= 3500 and daya <=5500 :
        tagihan = (pemakaian*1699.53)
    else :
        print ('data tidak valid')
if golongan == 'R3' :
    if daya >= 6600 :
        tagihan = (pemakaian*1699.53)
    else :
        print ('data tidak valid')
if golongan == 'B2' :
    if daya >= 6600 and daya <=200000 :
        tagihan = (pemakaian*1444.70)
    else :
        print ('data tidak valid')
if golongan == 'B3' :
    if daya >= 2000000 :
        tagihan = (pemakaian*1114.74)
if golongan == 'I3' :
    if daya >= 2000000 :
        tagihan = (pemakaian*1314.12)
    else :
        print ('data tidak valid')
if golongan == 'P1' :
    if daya >= 6600 and daya <=200000 :
        tagihan = (pemakaian*1523.28)
    else :
        print ('data tidak valid')

print (f'jumlah tagihan anda :{tagihan}')



