class Person :
	
	def __init__(self, name, age, isMale):
		self.name = name
		self.age = age
		self.isMale = isMale
		
	def setAge(self, age) :
		self.age = age
		
	def setName(self, name) :
		self.name = name
		
	def setGender(self, isMale) :
		self.isMale = isMale
		
	def getAge(self) :
		return self.age
		
	def getName(self) :
		return self.name
		
	def getGender(self) :
		return self.isMale
		
name = str(input())
age = int(input())
isMale = bool(input())

person1 = Person(name, age, isMale)

print(person1.getName())
print(person1.getAge())
print(person1.getGender())