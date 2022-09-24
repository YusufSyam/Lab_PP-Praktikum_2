import math

h = int(input(""))
a = int(input(""))
b = int(input(""))
print("")

if 90>a and a>b:
	c = math.tan(a*(math.pi/180))*h
	d = math.tan(b*(math.pi/180))*h
	e = c-d
	print(round(e, 1), "m")
else :
	print("Nilai tidak memungkinkan")