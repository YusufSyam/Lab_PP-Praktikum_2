x= int(input("Masukkan angka : "))
y= int(input("Masukkan angka : "))

if y%x != 0 :
    line_total = int((y//x)+1)
elif y%x == 0 :
    line_total = int((y/x)+1)

datas = []
for i in range(1,y+1) :
    datas.append(i)
for j in range(0,line_total):
    output= (datas[j*x:(j*x)+x])
    s=' '.join([str(elem) for elem in output])
    print(s)