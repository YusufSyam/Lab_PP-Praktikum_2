def getFPB(a, b):
    if a > b:
        c = a
    else:
        c = b
    for i in range(1, c+1):
        if a % i == 0 and b % i == 0:
            fpb = i            
    return fpb

a = int(input())
b = int(input())
print()
print(f"FPB ({a},{b}) = {getFPB(a, b)}")