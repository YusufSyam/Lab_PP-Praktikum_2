a = int(input(""))
b = int(input(""))
def getFPB(a, b):
    #saat y sama dengan nol maka return nilai a
    if (b == 0):
        return a
    #rekurens : saat y belum mencapai 0, maka terjadi rekursi
    else:
        return getFPB(b, a % b)

print(f"FPB ({a}, {b}) = {getFPB(a, b)}")
getFPB(a, b)