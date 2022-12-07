class Kubus:
    def __init__(self, lebar, tinggi, panjang, massa):
        self.lebar = lebar
        self.tinggi = tinggi
        self.panjang = panjang
        self.massa = massa
    def setMassa(self, massa):
        self.massa = massa
    def getMassaJenis(self):
        return self.massa / (self.lebar * self.tinggi * self.panjang)
lebar = float(input('Lebar: '))
tinggi = float(input('Tinggi: '))
panjang = float(input('Panjang: '))
massa = float(input('Massa: '))

kubus = Kubus (lebar, tinggi, panjang, massa)

kubus.setMassa(massa)
print('massa jenis = ', kubus.getMassaJenis())

kubus.setMassa(massa*2)
print('massa jenis = ', kubus.getMassaJenis())