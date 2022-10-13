x = int(input(" "))


def hitung_faktorial (x):
    if x > 2:
        return x * hitung_faktorial(x - 1)
    return 2

faktorial = hitung_faktorial(x)
print(f'{faktorial}')