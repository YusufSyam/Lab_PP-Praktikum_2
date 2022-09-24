from dataclasses import replace


print('\n==============================')
print('   PROGRAM TAGIHAN LISTRIK   ')
print('==============================')

golongan =(input('\nGolongan = '))
daya = float(input('Daya= '))
pemakaian = float(input('Pemakaian = '))
tagihan = pemakaian

if golongan == 'R1':
    if daya == 900 :
        tarif= 1352
        tagihan = pemakaian*tarif
        tagihan = "Jumlah tagihan anda : {:_}".format(tagihan)
        print (tagihan.replace('.',',').replace('_','.'))
    elif daya==1300 :
        tarif= 1444.70
        tagihan = pemakaian*tarif
        tagihan = "Jumlah tagihan anda : {:_}".format(tagihan)
        print (tagihan.replace('.',',').replace('_','.'))
    elif daya==2200:
        tarif= 1444.70
        tagihan = pemakaian*tarif
        tagihan = "Jumlah tagihan anda : {:_}".format(tagihan)
        print (tagihan.replace('.',',').replace('_','.'))
    else : 
        print ('Data tidak valid')
elif golongan == 'R2':
    if daya >=3500 and daya<=5500 :
        tarif= 1699.53
        tagihan = pemakaian*tarif
        tagihan = "Jumlah tagihan anda : {:_}".format(tagihan)
        print (tagihan.replace('.',',').replace('_','.'))
    else :
        print ('Data tidak valid')
elif golongan == 'R3':
    if daya>=6600 :
        tarif= 1699.53
        tagihan = pemakaian*tarif
        tagihan = "Jumlah tagihan anda : {:_}".format(tagihan)
        print (tagihan.replace('.',',').replace('_','.'))
    else : 
        print ('Data tidak valid')
elif golongan == 'B2':
    if daya>=6600 and daya<=200000:
        tarif= 1444.70
        tagihan = pemakaian*tarif
        tagihan = "Jumlah tagihan anda : {:_}".format(tagihan)
        print (tagihan.replace('.',',').replace('_','.'))
    else :
        print ('Data tidak valid')
elif golongan == 'B3':
    if daya>200000:
        tarif= 1114.74
        tagihan = pemakaian*tarif
        tagihan = "Jumlah tagihan anda : {:_}".format(tagihan)
        print (tagihan.replace('.',',').replace('_','.'))
    else :
        print ('Data tidak valid')
elif golongan == 'I3':
    if daya>=200000:
        tarif= 1314.12
        tagihan = pemakaian*tarif
        tagihan = "Jumlah tagihan anda : {:_}".format(tagihan)
        print (tagihan.replace('.',',').replace('_','.'))
    else : 
        print ('Data tidak valid')
elif golongan == 'P1':
    if daya>=6600 and daya<=200000:
        tarif= 1523.28
        tagihan = pemakaian*tarif
        tagihan = "Jumlah tagihan anda : {:_}".format(tagihan)
        print (tagihan.replace('.',',').replace('_','.'))
    else :
        print ('Data tidak valid')
else:
    print ('Data tidak valid')