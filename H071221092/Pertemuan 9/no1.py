class Human:
    def __init__(self, name, position):
        self.name = name
        self._pos_x = position  #private klo dua _
    def setName (self, name):
        self.name = name
    def getName (self):
        return self.name
    def getPosition (self):
        return self.__pos_x
    def setMovement (self, move):
        if move == 'L':
            self.__pos_x -= self._speed
        if move == 'R':
            self.__pos_x += self._speed #karena dua yg apakn kt bkin kan kondisi di soal hrus menerima r dan l 
    
class Hero (Human):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)  #super untuk memanggil method yg kita definisikan di parent class
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    def attack (self, target):
        target._health -= self._power
    
    def setPower (self, power):
        self._power = power

    def getPower (self):
        return self._power
    
    def setHealth (self, health):
        self._health = health

    def getHealth (self):
        return self._health

    def setArmor (self, armor):
        self._armor = armor

    def getArmor (self):
        return self._armor

    def setSpeed (self, speed):
        self._speed = speed

    def getSpeed (self):
        return self._speed

class Warrior (Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 26
        self._armor = 30

    def special (self, target):   #special itu method 
        self._power = 32
        self._armor = 45
        target._health -= self._power

class Assasin (Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 35
        self._speed = 4

    def special (self, target):   #special itu yang akan di ubah 
        self._speed = 7
        self._power = 42
        target._health -= self._power

class Support (Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._health = 500
        self._armor = 8
        self._speed = 4

    def special (self, target):
        self._speed = 6
        target._health += 150

    def setHealth(self, health):
        self._health = health
    
    def getHealth(self):
        return self._health

    def setArmor(self, armor):
        self._armor = armor
    
    def getArmor(self):
        return self._armor 

    def setSpeed(self, speed):
        self._speed = speed

    def getSpeed(self):
        return self._speed