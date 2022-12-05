class General :
	def __init__(self, health, attack, defense) :
		self._health = health
		self._attack = attack
		self._defense = defense
		
	def setHealth(self, health) :
		self._health = health
		
	def getHealth(self) :
		return self._health
		
	def setAttack(self, attack) :
		self._attack = attack
		
	def getAttack(self) :
		return self._attack
		
	def setDefense(self, defense):
		self._defense = defense
		
	def getDefense(self) :
		return self._defense

	def special() :
		pass

class Leonidas(General) :
	def __init__(self) :
		self._health = 500
		self._attack = 200
		self._defense = 300
	
	def special(self, target) :
		target.setAttack(target.getAttack() - 100)
		
class Alexander(General) :
	def __init__(self) :
		self._health = 350
		self._attack = 400
		self._defense = 250
	
	def special(self, target) :
		target.setDefense(target.getDefense() - 100)
		
class Khalid(General) :
	def __init__(self) :
		self._health = 400
		self._attack = 350
		self._defense = 250
		
	def special(self, target) :
		target.setDefense(target.getDefense() - 100)

class Lionheart(General) :
	def __init__(self) :
		self._health = 250
		self._attack = 450
		self._defense = 300
	
	def special(self, target) :
		target.setHealth(target.getHealth() - 100)

class Hannibal(General) :
	def __init__(self) :
		self._health = 300
		self._attack = 450
		self._defense = 250
		
	def special(self) :
		self._health += 100
	
			
khalid = Khalid()
leonidas = Leonidas()

print("Khalid Health (before) :", khalid.getHealth())
print("Khalid Attack (before) :", khalid.getAttack())
print("Khalid Defense (before) :", khalid.getDefense())
print()
print("Leonidas Health (before) :", leonidas.getHealth())
print("Leonidas Attack (before) :", leonidas.getAttack())
print("Leonidas Defense (before) :", leonidas.getDefense())

print("-"*20)
khalid.special(leonidas)
leonidas.special(khalid)

print("Khalid Health (after) :", khalid.getHealth())
print("Khalid Attack (after) :", khalid.getAttack())
print("Khalid Defense (after) :", khalid.getDefense())
print()
print("Leonidas Health (after) :", leonidas.getHealth())
print("Leonidas Attack (after) :", leonidas.getAttack())
print("Leonidas Defense (after) :", leonidas.getDefense())