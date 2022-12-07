class Person :
    def __init__(self,name,age,ismale) :
        self.name = name
        self.age = age
        self.ismale = ismale
    
    def setName(self, newName):
        self.name= newName
        
    def setAge(self, newAge):
        self.age= newAge
    
    def setIsmale(self, newIsmale):
        self.ismale= newIsmale

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getIsmale(self):
        return self.ismale

name = str(input("name :"))
age = int(input("age :"))
ismale = bool(input("male or not :"))

a= Person(name,age,ismale)
print (a.getName())
print (a.getAge())
print (a.getIsmale())