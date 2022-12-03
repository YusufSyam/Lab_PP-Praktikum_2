class Kubus:
    def __init__(self, lebar, tinggi, panjang):
        self.lebar = lebar
        self.tinggi = tinggi
        self.panjang = panjang
    
    def setLebar(self, lebar):
        self.lebar = lebar
    def setTinggi(self,tinggi):
        self.tinggi = tinggi
    def setPanjang(self, panjang):
        self.panjang = panjang
    def setMassa(self, massa):
        self.massa = massa

    def getMassaJenis(self):
        return self.massa/(self.panjang*self.lebar*self.tinggi)

lebar = float(input())
tinggi = float(input())
panjang = float(input())
massa = float(input())

kubus = Kubus(lebar, tinggi, panjang)

kubus.setMassa(massa)
print("Massa jenis =", kubus.getMassaJenis())
kubus.setMassa(massa*2)
print("Massa jenis =", kubus.getMassaJenis())