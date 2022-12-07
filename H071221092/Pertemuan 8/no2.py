class Kubus :
    def __init__(self, lebar, tinggi, panjang, massa) :
                self.lebar = lebar #atribut
                self.tinggi = tinggi 
                self.panjang = panjang 
                self.massa = massa
                self.massaJenis = 0 
    def setlebar (self, lebar) :
                self.lebar = lebar
    def settinggi (self, tinggi) :
                self.tinggi = tinggi 
    def setpanjang (self, panjang) :
                self.panjang = panjang 
    def setmassa (self, massa) :
                self.massa = massa 
    def setmassaJenis (self,massaJenis) :
                self.massaJenis = massaJenis 
    def getlebar (self) :
                return self.lebar 
    def gettinggi (self) :
                return self.tinggi
    def getpanjang (self) :
                return self.panjang 
    def getmassa (self) :
                return self.massa
    def getmassaJenis (self) :
                return self.massa / (self.panjang * self.lebar * self.tinggi)

lebar = float(input())
tinggi = float(input())
panjang = float(input())
massa = float(input())

kubus = Kubus(lebar, tinggi, panjang, massa) #objek

kubus.setmassa(massa)
print("Massa Jenis =", kubus.getmassaJenis())

kubus.setmassa(massa*2)
print("Massa Jenis =", kubus.getmassaJenis())