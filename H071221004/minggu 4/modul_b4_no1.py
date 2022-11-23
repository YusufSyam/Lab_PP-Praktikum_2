n = int(input(""))

def faktorial(n):
    #jika n sama dengan nol, maka nilai nya dikembalikan jadi 1
    if n == 0:
        return 1
    else:
        return n*faktorial(n-1)

print(faktorial(n))
faktorial(n)