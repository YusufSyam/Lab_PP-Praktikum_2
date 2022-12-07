a = input()+'.txt'
b = input()+'.txt'
try:
    with open (a) as asli:
        file_as = asli.readlines()
        n = []
        file_as[-1] += " "
        for x in file_as:
            n.append(len(x))
            with open(b, "w") as salinan:
                for i in file_as:
                    salinan.write(i.rjust(max(n)))
    print('berhasil')
except:
    print('invalid')