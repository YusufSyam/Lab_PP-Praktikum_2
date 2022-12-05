class Kubus :
    def __init__(self,lebar,tinggi,panjang) :
        self.lebar = lebar
        self.tinggi = tinggi
        self.panjang = panjang
    
    def setLebar(self, newLebar):
        self.lebar= newLebar
        
    def setTinggi(self, newTinggi):
        self.tinggi= newTinggi
    
    def setPanjang(self, newPanjang):
        self.panjang= newPanjang
        
    def setMassa(self, newMassa):
        self.massa= newMassa

    def getMassaJenis(self):
        return self.massa/(self.panjang*self.lebar*self.tinggi)

lebar = float(input())
tinggi = float(input())
panjang = float(input())
massa = float(input())

kubus = Kubus (lebar,tinggi,panjang)

kubus.setMassa(massa)
print ("Massa Jenis =",kubus.getMassaJenis())
kubus.setMassa(massa*2)
print ("Massa Jenis =",kubus.getMassaJenis())