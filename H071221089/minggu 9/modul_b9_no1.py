class Human :
    def __init__(self,name,position) :
        self.name = name
        self._position = position

    def setMovement (self,move) :
        if move == 'l' :
            self._position -= self._speed
        if move == 'r' :
            self._position += self._speed

    def getMovement (self) :
        return self._position

class Hero (Human) :
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    def attack (self,target) :
        target.setHealth (target.getHealth()-self._power)
        
    def setPower (self,power) :
        self._power = power

    def setHealth (self,health) :
        self._health = health

    def setArmor (self,armor) :
        self._armor = armor
    
    def setSpeed (self,speed) :
        self._speed = speed

    def getPower (self):
        return self._power

    def getHealth (self):
        return self._health

    def getArmor (self):
        return self._armor

    def getSpeed (self):
        return self._speed

class Warrior (Hero) :
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 26
        self._armor = 30
    
    def special (self,target) :
        self._armor = 45
        self._power = 32
        target.setHealth (target.getHealth()-self._power)

class Assassin (Hero) :
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 35
        self._speed = 4

    def special (self,target) :
        self._speed = 7
        self._power = 42
        target.setHealth (target.getHealth()-self._power)

class Support (Hero) :
    def __init__(self, name, position):
        super().__init__(name, position)
        self._health = 500
        self._armor = 8
        self._speed = 4

    def special (self,target) :
        self._speed = 6
        target.setHealth (target.getHealth()+ 150)
        
warrior = Warrior ("bambang", position=10)
assassin = Assassin ("joko", position=25)
support = Support ("udin", position=30)

print ("health (before)",warrior.getHealth())
assassin.attack (warrior)
print ("health (after)",warrior.getHealth())
print ("-"*10)

print ("Warrior (health)",warrior.getHealth())
print ("Support (speed)",support.getSpeed())
support.special (warrior)

print ("Warrior (health)",warrior.getHealth())
print ("Support (speed)",support.getSpeed())


