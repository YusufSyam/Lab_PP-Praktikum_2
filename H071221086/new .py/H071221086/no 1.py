a = int(input('masukkan nilai n: '))
if a % 3 ==0:
    if a <= 0:
        print(f'{a} berada pada kelompok A1')
    elif a > 0 and a<= 100:
        print(f'{a} berada pada kelompok B1')
    elif a > 100 and a<= 200:
        print(f'{a} berada pada kelompok C1')
    elif a > 200:
        print(f"{a} berada pada kelompok D1")

if a % 3 ==1:
    if a <= 0:
        print(f'{a} berada pada kelompok A2')
    elif a > 0 and a<= 100:
        print(f'{a} berada pada kelompok B2')
    elif a > 100 and a<= 200:
        print(f'{a} berada pada kelompok C2')
    elif a > 200:
        print(f"{a} berada pada kelompok D2")

if a % 3 ==2:
    if a <= 0:
        print(f'{a} berada pada kelompok A3')
    elif a > 0 and a<= 100:
        print(f'{a} berada pada kelompok B3')
    elif a > 100 and a<= 200:
        print(f'{a} berada pada kelompok C3')
    elif a > 200:
        print(f"{a} berada pada kelompok D3")
