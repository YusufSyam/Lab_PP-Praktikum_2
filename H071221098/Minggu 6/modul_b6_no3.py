x = (input()) + '.txt'
y = int(input())

with open (x,'w') as tabel:
    
    with open (x, 'w') as origin : 
        origin.write('\n+------------------------+------------+----------+')
        origin.write('\n|           nama         |    nim     +angkatan  |')
        origin.write('\n+------------------------+------------+----------+')

        for i in range(y):
            a = input().replace(" ","_")
            b = input()
            c = input()
            if len(a) > 20 or len(b) > 10 or len(c) > 4:
                print('gagal')
                exit()
        else:
            origin.write(f"\n|{a.ljust(24)}|{b.ljust(12)}|{c.ljust(10)}|")

        origin.write('\n+------------------------+------------+----------+')
        print('berhasil')