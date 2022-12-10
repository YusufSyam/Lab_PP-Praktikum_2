def myDay(a):
    while a >= 365 :
        b = a // 365
        a = a % 365
    while a >= 30 :
        c = a // 30
        a = a % 30
    while c >= 12 :
        c = c - 12
        b = b + 1
    print(f"{b} tahun")
    print(f"{c} bulan")
    print(f"{a} hari")

a = int(input())
print()
print(myDay(a))