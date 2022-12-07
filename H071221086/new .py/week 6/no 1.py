a = input()
b = input()
c = open(f'{a}.txt','r')
d = c.read()

try:
    with open(f'{b}.txt','w') as file:
        file.write(d)
        print('berhasil')
except:
    print('tidak berhasil')