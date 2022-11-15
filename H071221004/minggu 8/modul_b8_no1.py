inputName=input('Name: ')
inputAge=int(input('Age: '))
inputIsmale=eval(input(('Is Male: ')))
print()

class person :

    def __init__(self, inputName,inputAge,inputGender) :
        self.name=inputName
        self.age=inputAge
        self.isMale=inputGender

    def setName(self,inputName) :
        self.name=inputName

    def getName(self) :
        print('Name:', self.name)

    def setAge(self, inputAge) :
        self.age=inputAge
    def getAge(self) :
        print('Age:', self.age)

    def setGender(self,inputGender) :
        self.isMale=inputGender

    def getGender(self) :
        if self.isMale == True:
            print('Gender: Male')
        elif self.isMale == False:
            print('Gender: Female')
        else :
            print('Please make sure you put True/False in Is Male.')

person1=person(inputName, inputAge, inputIsmale)
person1.setName()
person1.getName()
person1.setAge()
person1.getAge()
person1.setGender()
person1.getGender()

#person1.setName(input("Masukkan nama baru: "))
#person1.setAge(int(input("Masukkan umur baru: ")))
#person1.setGender(eval(input("Masukkan gender baru: ")))

#print("Data Baru: ")

#person1.getName()
#person1.getAge()
#person1.getGender()