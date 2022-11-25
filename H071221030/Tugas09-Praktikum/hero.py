class Human :
	def __init__(self, name, pos_x):
		self.name = name
		self.__pos_x = pos_x
		
	def setName(self, name) :
		self.name = name
		
	def getName(self) :
		return self.name
		
	def setMovement(self, pos_x):
		if pos_x == "L" :
			self._pos_x -= self._speed
		elif pos_x == "R" :
			self._pos_x += self._speed
			
	def getMovement(self):
		return self.pos_x
	
class Hero(Human) :
	def __init__(self, name, pos_x) :
		super().__init__(name, pos_x)
		self._power = 15
		self._health = 400 
		self._armor = 15
		self._speed = 3
		
	def setPower(self, power) :
		self._power = power
		
	def getPower(self) :
		return self._power
		
	def setHealth(self, health) :
		self._health = health
		
	def getHealth(self) :
		return self._health
		
	def setArmor(self, armor) :
		self._armor = armor
		
	def getArmor(self) :
		return self._armor	 
		
	def setSpeed(self, speed) :
		self._speed = speed
		
	def getSpeed(self) :
		return self._speed
		
	def attack(self, target):
		target.setHealth(target.getHealth() - self._power)
		
class Warrior(Hero) :
	def __init__(self, name, pos_x):
		super().__init__(name, pos_x)
		self._power = 26
		self._armor = 30
		
	def special(self, target):
		self.setArmor(45)
		self.setPower(32)
		target.setHealth(target.getHealth() - self._power)
		
class Assassin(Hero) :
	def __init__(self, name, pos_x):
		super().__init__(name, pos_x)
		self._power = 35
		self._speed = 4
	
	def special(self, target):
		self.setSpeed(7)
		self.setPower(42)
		target.setHealth(target.getHealth() - self._power)
		
class Support(Hero) :
	def __init__(self, name, pos_x):
		super().__init__(name, pos_x)
		self._health = 500
		self._armor = 8
		self._speed = 4
		
	def special(self, target):
		self.setSpeed(6)
		target.setHealth(target.getHealth() + 150)