a = int(input("Input nilai matriks pertama index 1,1: "))
b = int(input("Input nilai matriks pertama index 1,2: "))
c = int(input("Input nilai matriks pertama index 2,1: "))
d = int(input("Input nilai matriks pertama index 2,2: "))
e = int(input("Input nilai matriks pertama index 1,1: "))
f = int(input("Input nilai matriks pertama index 1,2: "))
g = int(input("Input nilai matriks pertama index 2,1: "))
h = int(input("Input nilai matriks pertama index 2,2: "))

x = [
    [a, b],
    [c, d],
]
y = [
    [e, f],
    [g, h],
]
p = [
    [(a*e) + (b*g), (a*f) + (b*h)],
    [(c*e) + (d*g), (c*f) + (d*h)],
]

for i in range(2):
    if i == 0:
        print(x[i], "x", y[i], "=", p[i])
    else:
        print(x[i], " ", y[i], " ", p[i])