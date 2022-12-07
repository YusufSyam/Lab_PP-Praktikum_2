def convert(x):
    if x == "True":
        return 1
    else: return 0

def gol(n1,n2):
    psm = sum(n2)
    real = sum(n1)
    if psm > real :
        print("PSM Makassar")
    elif real > psm:
        print("Real Madrid")
    # else: print("Se
    
n1 = list(map(convert,input().split()))
n2 = list(map(convert,input().split()))
# print(n1,n2)
gol(n1,n2)