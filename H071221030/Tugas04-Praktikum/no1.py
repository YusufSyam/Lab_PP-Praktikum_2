a = int(input())

x = 0

for i in range(2, a):
    if a % i == 0:
        x = x + 1

print()
if x >= 1 :
    print("Ini bukan bilangan prima")
elif a == 1 or a == -1 :
    print("Ini bukan bilangan prima")
else : 
    print("Ini bilangan prima")