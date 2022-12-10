class Person :
    def __init__(self):
        self.name = ""
        self.nama = ""
        self.age = 0
        self.isMale = True
        self.prodi = ""
        self.alamat = ""
        self.asal = ""
    def setName (self,name) :
        self.name = name
    def getName (self) :
        return self.name
    def setAge (self,age) :
        self.age = age
    def getAge (self) :
        return self.age
    def setNama (self,nama) :
        self.nama = nama
    def getNama (self) :
        return self.nama
    def setGender (self, gender ) :
        if gender == "laki-laki" :
            self.isMale = True
            self.gender = "laki-laki"
        elif gender == "perempuan" :
            self.isMale = False
            self.gender = "perempuan"
        else :
            print("inputan salah")
    def getGender (self) :
        return self.gender
    def setProdi(self, prodi) :
        self.prodi = prodi 
    def getProdi(self) :
        return self.prodi
    def setAlamat(self, alamat) :
        self.alamat = alamat
    def getAlamat(self) :
        return self.alamat
    def setAsal(self, asal) :
        self.asal = asal
    def getAsal(self) :
        return self.asal
    def sayHello(self,targetName) :
        print(f"Halo {targetName} saya {self.name}")

name = input("Masukkan Nama :")
nama = input ("Masukkan Nama :")
age = int(input("Masukkan umur :"))
gender = input("Masukkan gender :")
prodi = input("Masukkan prodi :")
alamat = input ("Masukkan Alamat :")
asal = input ("Masukkan asal :")

person1 = Person()
person2 = Person()

person1.setName (name)
person1.setAge (age)
person1.setGender(gender) 
person1.setProdi (prodi)
person1.setAlamat (alamat)
person1.setAsal (asal)
person2.setNama (nama)

person1.sayHello(person2.nama)

print (person1.getName())
print (person1.getAge())
print (person1.getGender())
print (person1.getProdi())
print (person1.getAlamat ())
print (person1.getAsal())
print (person2.getNama())

print (person1.isMale)