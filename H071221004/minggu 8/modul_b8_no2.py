lebar=float(input())
tinggi=float(input())
panjang=float(input())
massa=float(input())

class Kubus :
    def __init__(self,inputLebar,inputTinggi,inputPanjang,inputMassa) :
        self.lebar=inputLebar
        self.tinggi=inputTinggi
        self.panjang=inputPanjang
        self.massa=inputMassa

    def setLebar(self,inputLebar):
        self.lebar= inputLebar

    def getLebar(self):
        return self.lebar
        
    def setTinggi(self,inputTinggi):
        self.tinggi=inputTinggi

    def getTinggi(self):
        return self.tinggi

    def setPanjang(self,inputPanjang):
        self.panjang=inputPanjang

    def getPanjang(self):
        return self.panjang

    def setMassa(self,inputMassa):
        self.massa=inputMassa

    def getMassa(self):
        return self.massa
        

    def getMassaJenis(self):
        self.massaJenis=self.massa/(self.panjang*self.lebar*self.tinggi)
        return self.massaJenis


kubus=Kubus(lebar,tinggi,panjang,massa)
print('Massa Jenis =', kubus.getMassaJenis())
kubus.setMassa(massa*2)
print('Massa Jenis =', kubus.getMassaJenis())