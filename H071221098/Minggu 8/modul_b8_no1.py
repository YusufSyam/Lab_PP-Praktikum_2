class Person:
    def __init__(self, name, age, isMale):
        self.name = name
        self.age = age
        self.isMale = isMale
    
    def setName(self, name):
        self.name = name
    def setAge(self,age):
        self.age = age
    def setIsMale(self, isMale):
        self.isMale = isMale

    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getGender(self):
        return self.isMale

name = str(input("Name: "))
age = int(input("Age: "))
isMale = bool(input("Male or not: "))

person1 = Person(name, age, isMale)

print(person1.getName())
print(person1.getAge())
print(person1.getGender())


