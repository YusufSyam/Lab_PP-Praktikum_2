x = int(input(" "))

if x > 1:
    for i in range (2, x):
        if x % i == 0:
            print("bukan bilangan prima")
            print(i, "kali", x//i, "=", x)
            break
    else:
        print("Ini bilangan prima")
else:
    print("bukan bilangan prima")
