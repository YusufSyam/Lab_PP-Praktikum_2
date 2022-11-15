x, y=0, 0
s= input()

def move(i, x, y):
    if i == "R" :
        x=x+1

    elif i == "L" :          
        x=x-1  
        
    elif i == "U" :
        y=y+1
    
    elif i == "D" :
        y=y-1
    
    return x, y


print(x, y)
for i in s:
    x, y= move(i, x, y)
    print(x, y)










