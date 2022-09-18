
class hamburger:
    nama =""
    harga = 0
    jumlah = 0
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        self.jumlah = 1

    def total(self):
        return harga*jumlah

    def setJumlah(self, jumlah):
        self.jumlah= jumlah

    def getJumlah(self):
        return self.jumlah

    def totalHarga(self):
        return self.harga*self.jumlah

    def option(self):
        print("---------------------------------------------")
        print("1. pesan")
        print("2. Menu Tambahan")
        print("3. kembali")
        print("---------------------------------------------")

    def showMenu(self):
        print(" ____________________________________________")
        print("|        SELAMAT DATANG DI BURGER STORE      |")
        print("|                Daftar Pesanan              |")
        print("|____________________________________________|")
        print("1. Hamburger Original\t\tRp. 10.000")
        print("2. Hamburger Ayam\t\tRp. 14.000")
        print("3. Hamburger Keju\t\tRp. 13.000")
        print("4. Hamburger Super\t\tRp. 20.000")
        print("5. Exit")
        print("---------------------------------------------")

class additon(hamburger):
    pass
    def showAddition(self):
        print("____________________________________________")
        print("|               Menu Tambahan               |")
        print("|___________________________________________|")
        print("1. Air Mineral\t\t\tRp. 5.000")
        print("2. Soda\t\t\t\tRp. 7.000")
        print("3. Es Teh\t\t\tRp. 5.500")
        print("4. Thai Tea\t\t\tRp. 8.000")
        print("5. GreenTea\t\t\tRp. 9.000")
        print("6. Cokelat\t\t\tRp. 7.000")
        print("7. Susu\t\t\t\tRp. 6.000")
        print("---------------------------------------------")

a = hamburger("Hamburger Original", 10000)
b = hamburger("Hamburger Ayam", 14000)
c = hamburger("Hamburger Keju", 13000)
d = hamburger("Hamburger Super", 20000)

g = additon("air", 5000)
h = additon("soda", 7000)
i = additon("es teh", 5500)
j = additon("tai tea", 8000)
k = additon("green tea", 9000)
l = additon("cokelat", 7000)
m = additon("susu", 6000)

menu = hamburger("main Menu", 0)
add = additon("additon", 0)
opsi = hamburger("option", 0)

booleanUlang = True
while booleanUlang == True:
    menu.showMenu()
    entry1 = int(input(">> "))

    if entry1==1:
        print("Hamburger Original, harga Rp. 10.000")
        entry2 = int(input("Jumlah pesanan : "))
        a.setJumlah(entry2)
        opsi.option()
        entry3 = int(input(">> "))
        if entry3 == 1:
            print("Total Harga : Rp. {}".format(a.totalHarga()))
        elif entry3 == 2:
            add.showAddition()
            entry4 = int(input(">> "))
            if entry4 == 1:
                print("Total Harga : Rp. {}".format(a.totalHarga()+g.totalHarga()))
            elif entry4 ==2:
                print("Total Harga : Rp. {}".format(a.totalHarga()+h.totalHarga()))
            elif entry4 ==3:
                print("Total Harga : Rp. {}".format(a.totalHarga()+i.totalHarga()))
            elif entry4 ==4:
                print("Total Harga : Rp. {}".format(a.totalHarga()+j.totalHarga()))
            elif entry4 ==5:
                print("Total Harga : Rp. {}".format(a.totalHarga()+k.totalHarga()))
            elif entry4 ==6:
                print("Total Harga : Rp. {}".format(a.totalHarga()+l.totalHarga()))
            elif entry4 ==7:
                print("Total Harga : Rp. {}".format(a.totalHarga()+m.totalHarga()))
            else:
                continue
        else:
            continue

        print("continue?(y/n)")
        nex = input(">> ")
        if nex == "y":
            continue
        else:
            break

    if entry1==2:
        print("Hamburger Ayam, harga Rp. 14.000")
        entry2 = int(input("Jumlah pesanan : "))
        b.setJumlah(entry2)
        opsi.option()
        entry3 = int(input(">> "))
        if entry3 == 1:
            print("Total Harga : Rp. {}".format(b.totalHarga()))
        elif entry3 == 2:
            add.showAddition()
            entry4 = int(input(">> "))
            if entry4 == 1:
                print("Total Harga : Rp. {}".format(b.totalHarga()+g.totalHarga()))
            elif entry4 ==2:
                print("Total Harga : Rp. {}".format(b.totalHarga()+h.totalHarga()))
            elif entry4 ==3:
                print("Total Harga : Rp. {}".format(b.totalHarga()+i.totalHarga()))
            elif entry4 ==4:
                print("Total Harga : Rp. {}".format(b.totalHarga()+j.totalHarga()))
            elif entry4 ==5:
                print("Total Harga : Rp. {}".format(b.totalHarga()+k.totalHarga()))
            elif entry4 ==6:
                print("Total Harga : Rp. {}".format(b.totalHarga()+l.totalHarga()))
            elif entry4 ==7:
                print("Total Harga : Rp. {}".format(b.totalHarga()+m.totalHarga()))
            else:
                continue
        else:
            continue

        print("continue?(y/n)")
        nex = input(">> ")
        if nex == "y":
            continue
        else:
            break

    if entry1==3:
        print("Hamburger Keju, harga Rp. 13.000")
        entry2 = int(input("Jumlah pesanan : "))
        c.setJumlah(entry2)
        opsi.option()
        entry3 = int(input(">> "))
        if entry3 == 1:
            print("Total Harga : Rp. {}".format(c.totalHarga()))
        elif entry3 == 2:
            add.showAddition()
            entry4 = int(input(">> "))
            if entry4 == 1:
                print("Total Harga : Rp. {}".format(c.totalHarga()+g.totalHarga()))
            elif entry4 ==2:
                print("Total Harga : Rp. {}".format(c.totalHarga()+h.totalHarga()))
            elif entry4 ==3:
                print("Total Harga : Rp. {}".format(c.totalHarga()+i.totalHarga()))
            elif entry4 ==4:
                print("Total Harga : Rp. {}".format(c.totalHarga()+j.totalHarga()))
            elif entry4 ==5:
                print("Total Harga : Rp. {}".format(c.totalHarga()+k.totalHarga()))
            elif entry4 ==6:
                print("Total Harga : Rp. {}".format(c.totalHarga()+l.totalHarga()))
            elif entry4 ==7:
                print("Total Harga : Rp. {}".format(c.totalHarga()+m.totalHarga()))
            else:
                continue
        else:
            continue

        print("continue?(y/n)")
        nex = input(">> ")
        if nex == "y":
            continue
        else:
            break

    if entry1==4:
        print("Hamburger Super, harga Rp. 20.000")
        entry2 = int(input("Jumlah pesanan : "))
        a.setJumlah(entry2)
        opsi.option()
        entry3 = int(input(">> "))
        if entry3 == 1:
            print("Total Harga : Rp. {}".format(d.totalHarga()))
        elif entry3 == 2:
            add.showAddition()
            entry4 = int(input(">> "))
            if entry4 == 1:
                print("Total Harga : Rp. {}".format(d.totalHarga()+g.totalHarga()))
            elif entry4 ==2:
                print("Total Harga : Rp. {}".format(d.totalHarga()+h.totalHarga()))
            elif entry4 ==3:
                print("Total Harga : Rp. {}".format(d.totalHarga()+i.totalHarga()))
            elif entry4 ==4:
                print("Total Harga : Rp. {}".format(d.totalHarga()+j.totalHarga()))
            elif entry4 ==5:
                print("Total Harga : Rp. {}".format(d.totalHarga()+k.totalHarga()))
            elif entry4 ==6:
                print("Total Harga : Rp. {}".format(d.totalHarga()+l.totalHarga()))
            elif entry4 ==7:
                print("Total Harga : Rp. {}".format(d.totalHarga()+m.totalHarga()))
            else:
                continue
        else:
            continue

        print("continue?(y/n)")
        nex = input(">> ")
        if nex == "y":
            continue
        else:
            break

    else:
        break