from math import floor

a = int(input(""))
print("")

jam = floor(a/3600) ; b = a-(3600*jam)
menit = floor(b/60)
detik = b-(60*menit)

print(jam, end = ':')
if menit < 10 :
    print("0", end = '')
    print(menit, end = ':')
    if detik < 10 :
        print("0", end = '')
        print(detik)
    else :
        print(detik)
else :
    print(menit, end = ':')
    if detik < 10 :
        print("0", end = '')
        print(detik)
    else :
        print(detik)