operasi = input().upper()

x = 0
y = 0

print (x, y)

for i in operasi:
        if i == "R":
            x = x + 1
            print(x, y)
        elif i == "L":
            x = x - 1
            print(x, y)
        elif i == "U":
            y = y + 1
            print(x, y)
        elif i == "D":
            y = y - 1
            print(x, y)