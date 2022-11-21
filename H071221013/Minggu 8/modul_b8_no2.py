lebar = float(input())
tinggi = float(input())
panjang = float(input())
massa = float(input())

class Kubus:

    def __init__(self, lebar, tinggi, panjang, massa):
        self.lebar = lebar
        self.tinggi = tinggi
        self.panjang = panjang
        self.massa = massa
        # self.massaJenis = massaJenis

    def setLebar(self, lebar):
        self.lebar = lebar

    def getLebar(self):
        return self.lebar

    def setTinggi(self, tinggi):
        self.tinggi = tinggi

    def getTinggi(self):
        return self.tinggi

    def setPanjang(self, panjang):
        self.panjang = panjang

    def getPanjang(self):
        return self.panjang

    def setMassa(self, massa):
        self.massa = massa

    def getMassa(self):
        return self.massa

    def getMassaJenis(self):
        return self.massa/(self.panjang*self.lebar*self.tinggi)

kubus = Kubus(lebar, tinggi, panjang, massa)

kubus.setMassa(massa)
print("Massa Jenis =", kubus.getMassaJenis())

kubus.setMassa(massa*2)
print("Massa Jenis =", kubus.getMassaJenis())

    





    
    
