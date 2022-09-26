golongan = input("golongan = ")
daya = int(input("daya = "))
pemakaian = int(input("pemakaian = "))

if (golongan == 'R1' or golongan == 'r1') and daya == 900:
    print(pemakaian * 1352)
elif (golongan == 'R1' or golongan == 'r1') and daya == 1300:
    print(pemakaian * 1444.70)
elif (golongan == 'R1' or golongan == 'r1') and daya == 2200:
    print(pemakaian * 1444.70)

elif (golongan == 'R2' or golongan == 'r2') and daya >= 3500 and daya <= 5500:
    print(pemakaian * 1699.53)

elif (golongan == 'R3' or golongan == 'r3') and daya >= 6600 and daya <= 6600:
    print(pemakaian * 1699.53)
elif (golongan == 'B2' or golongan == 'b2') and daya > 6600 and daya < 200000:
    print(pemakaian * 1444.70)
elif (golongan == 'B3' or golongan == 'b3') and daya >= 200000:
    print(pemakaian * 1114.74)
elif (golongan == 'I3' or golongan == 'i3') and daya >= 200000:
    print(pemakaian * 1314.12)
elif (golongan == 'P1' or golongan == 'p1') and daya >= 6600 and daya <= 200000:
    print(pemakaian * 1523.28)
else:
    print('Data tidak valid')
