from abc import ABC, abstractmethod

class Motor(ABC):
    @abstractmethod
    def helm(self):
        pass

    def __init__(self, produk, mesin):
        self.produk = produk
        self.__mesin = mesin

    def setMesin(self, mesin):
        self.__mesin = int(mesin)
    
    def getMesin(self):
        return self.__mesin

class Yamaha(Motor):
    def __init__(self, produk, mesin):
        super().__init__(produk, mesin)
        self.kecepatan = 105

    def setKecepatan(self, kecepatan):
        self.kecepatan = int(kecepatan)

    def melaju(self):
        print('Dapat melaju hingga',self.kecepatan,'km/jam')

    def helm(self):
        print('Beli Motor Yamaha gratis Helm')

class Honda(Motor):
    def __init__(self, produk, mesin):
        super().__init__(produk, mesin)
        self.kecepatan = 95
    
    def setKecepatan(self, kecepatan):
        self.kecepatan = int(kecepatan)

    def melaju(self):
        print('Dapat melaju hingga',self.kecepatan,'km/jam')

    def helm(self):
        print('Beli Helm gratis Motor Honda')

def test_kecepatan(motor):
    motor.melaju()

yamaha = Yamaha('Odong-odong', 110)
honda = Honda('Bentor', 110)

print('YAMAHA')
print(yamaha.produk + ' Keluaran terbaru dari Yamaha')
print(f'Dengan mesin {yamaha.getMesin()} cc')
#memanggil abstrak method
yamaha.helm()
#memanggil interface
test_kecepatan(yamaha)

print('\nHONDA')
print(honda.produk + ' Sedikit modifikasi dari Honda')
print(f'Dengan mesin {honda.getMesin()} cc')
#memanggil abstrak method
honda.helm()
#memanggil interface
test_kecepatan(honda)


