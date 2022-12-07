x = int(input('masukkan x: '))
y = int(input('masukkan y: '))
if x > 0 and x <= 10 and y > 0 and y <=10:
    print(f'koordinat : {x},{y} , berada pada kuadran 1')
elif x < 0 and x <= -10 and y > 0 and y <=10:
    print(f'koordinat : {x},{y} , berada pada kuadran 2')
elif x < 0 and x >= -10 and y < 0 and y >=-10:
    print(f'koordinat : {x},{y} , berada pada kuadran 3')
elif x < 0 and x <= 10 and y < 0 and y >=-10:
    print(f'koordinat : {x},{y} , berada pada kuadran 4')
elif x == 0 and y == 0:
    print(f'koordinat : ({x},{y}) , berada pada pusat koordinat')
elif x == 0 and y > 0 and y<= 10 or y <0 and y>= -10:
    print(f'koordinat : ({x},{y}) , berada pada garis y')
elif y == 0 and x > 0 and x <= 10 or x<0 and x >= -10:
    print(f'koordinat : ({x},{y}) , berada pada garis x')