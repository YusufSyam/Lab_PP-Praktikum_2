a = int(input(' '))
def myDay(a):
    Tahun = a//365
    sisa = a % 365
    Bulan = sisa // 30
    Hari = sisa % 30
    print('%d Tahun' % (Tahun))
    print('%d Bulan' % (Bulan))
    print('%d Hari' % (Hari))
myDay(a)