a = int(input(""))
def myDay(a):
    Tahun = a // 365
    sisa  = a % 365
    Bulan = sisa // 30
    Hari  = sisa % 30

    print("%d tahun" %(Tahun))
    print("%d bulan" %(Bulan))
    print("%d hari"  %(Hari))
myDay(a)