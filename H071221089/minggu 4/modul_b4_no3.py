
def  all_string_rotation():
    name = input()
    if (len(name) <= 1 ):
            return name
    else:
        for r in range(5):
            print(name[r:] + name[:r])
        
all_string_rotation()