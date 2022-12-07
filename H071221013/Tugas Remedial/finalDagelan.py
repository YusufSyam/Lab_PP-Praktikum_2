t1 = input().split()
t2 = input().split()

goll1 = 0
goll2 = 0
for i in t1:
    if i == "True":
        goll1+=1
    else:
        goll1+=0

for i in t2:
    if i == "True":
        goll2+=1
    else:
        goll2+=0
        
if goll1 > goll2:
    print("Real Madrid")
elif goll2 > goll1:
    print("PSM Makassar")
    