a = (input('input array ke 1: ').split())
b = (input('input array ke 2: ').split())
setnya_a = set(map(int,a))
setnya_b = set(map(int,b))
if len(setnya_a & setnya_b) == 0:
    print('tidak ada duplikat')
else:
    print(f'terdapat {len(setnya_a & setnya_b)} buah duplikat yaitu {setnya_a & setnya_b}'.replace('{','(').replace('}',')'))