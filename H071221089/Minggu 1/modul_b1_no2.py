def banner ():
    print (
'''=========================
    PROGRAM KONVERSI 
DETIK KE JAM,MENIT,DETIK
=========================''')
def main():
    n = int(input("masukkan detik : "))
    jam = int (n // 3600)
    menit = int (n - (jam*3600))// 60
    detik = int (n -(jam*3600 - (menit*60)))
    print ('%d jam,%d menit dan %d detik' %(jam,menit,detik))
def exit ():
    print (
"""============================
|       Thank You          |
============================""")

banner ()
main ()
exit ()