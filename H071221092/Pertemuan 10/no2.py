from abc import ABC, abstractmethod  # ketentuan(abstarctbaseclass)

class Wisata(ABC): #(class parents)
    @abstractmethod
    def oleholeh(self):
        pass
    def __init__(self, nama, harga):
        self.nama = nama
        self.__harga = harga
    def setHarga(self, harga):
        self.__harga = int(harga)
    def getHarga(self):
        return self.__harga

class Bali(Wisata): #Inheritance
    def __init__(self, nama, harga):
        super().__init__(nama, harga)
        self.harga = harga
        self.biaya = 10
    def setHarga(self, harga):
        self.harga = int(harga)
    def place(self):
        print('Total uang yang digunakan ialah', self.biaya, 'juta rupiah')
    def oleholeh(self):
        print('Oleh-oleh yang bisa dibawa pulang dari Bali ialah Joger,Pie Susu,Sarung Bali,Bule')
    def Keunggulan(self):
        print('Keunggulannya ialah terdapat seluncuran yang tinggi dan banyak wahana waterboom lainnya')

class Lombok(Wisata):
    def __init__(self, nama, harga):
        super().__init__(nama, harga)
        self.harga = harga
        self.biaya = 5
    def setHarga(self, harga):
        self.harga = int(harga)
    def place(self): #polyphorism
        print('Total uang yang digunakan ialah', self.biaya, 'juta rupiah')
    def oleholeh(self):
        print('Oleh-oleh yang bisa dibawa pulang dari Lombok ialah Manisan Rumput Laut dan Madu Sumbawa')
    def Keunggulan(self):
        print('Keunggulannya ialah warna pasirnya yang sangat cantik dan menarik')


def test_harga(wisata):
    wisata.place()

#kelas anakan
bali = Bali('Circus Waterpark Kuta Bali', 100)
lombok = Lombok('Pink Beach Lombok', 50)

print('BALI')
print(bali.nama + ' adalah tempat wisata di Bali')
print(f'Dengan harga masuk {bali.harga} ribu rupiah')
bali.Keunggulan()
# memanggil abstrak method
bali.oleholeh()
# memanggil interface
test_harga(bali)

print('\nLOMBOK')
print(lombok.nama + ' adalah tempat wisata di Lombok')
print(f'Dengan harga masuk {lombok.harga} ribu rupiah')
lombok.Keunggulan()
# memanggil abstrak method
lombok.oleholeh()
# memanggil interface
test_harga(lombok)