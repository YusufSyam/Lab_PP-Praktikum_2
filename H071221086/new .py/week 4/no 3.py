a = int(input(' '))
def myDay(a):
    tahun = a//365
    sisa = a % 365
    bulan = sisa // 30
    hari = sisa % 30
    print(f'{tahun} tahun')
    print(f'{bulan} bulan')
    print(f'{hari} hari')
myDay(a)
    
