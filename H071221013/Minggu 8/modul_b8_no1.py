class Person:
    def __init__(self, name, age, isMale):
        self.name = name
        self.age = age
        self.isMale = isMale

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age
    
    def getAge(self):
        return self.age

    def setisMale(self, isMale):
        self.isMale = isMale

    def getisMale(self):
        return self.isMale
    
name = input("Masukkan Name : ")
age = int(input("Masukkan Age : "))
ismale = eval(input("Masukkan isMale : "))

santi = Person(name, age, ismale)

print(santi.getName())
print(santi.getAge())
print(santi.getisMale())

santi.setName("A")
santi.setAge(9)
santi.setisMale(False)

print(santi.getName())
print(santi.getAge())
print(santi.getisMale())