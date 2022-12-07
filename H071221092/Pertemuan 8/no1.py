class data:
    def __init__(self, nama, umur, gender):
        self.nama = nama
        self.umur = umur
        self.gender = gender
    def getAge(self,umur):
        print(umur)
    def getName(self, nama):
        print(nama)
    def getGender(self, gender):
        print(gender)
        if gender == True:
            gender = 'Male'
            print(gender)
        else:
            gender = 'female'
            print(gender)
nama = input('Masukkan nama: ')
umur = (input('Masukkan umur: '))
gender = input('kamu male? True or False: ').lower()
if gender == 'true':
    gender = bool(True)
else:
    gender = bool(False)

data_diri = data(nama, umur, gender)
data_diri.getName(nama)
data_diri.getAge(umur)
data_diri.getGender(gender)