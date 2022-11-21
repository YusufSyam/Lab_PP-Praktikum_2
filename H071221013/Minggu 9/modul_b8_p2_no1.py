class Human:
    def __init__(self, name, position):
        self.name = name
        self.__pos_x = position
    

    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    def setPosition(self, position):
        self.__position = position
    
    def getPosition(self):
        return self.__position

    def setMovement(self, move):
        if move == "L":
            self.__pos_x -= self._speed
        elif move == "R":
            self.__pos_x += self._speed 
    
    def getMovement(self):
        return self.__pos_x


class Hero(Human):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3
    
    def attack(self, target):
        target.setHealth(target.getHealth() - self._power)

    def setPower(self, power):
        self._power = power 

    def getPower(self):
        return self._power

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


class Warrior(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 26
        self._armor = 30

    def special(self, target):
        self._power = 32
        self._armor = 45
        target.setHealth(target.getHealth() - self._power)

class Assassin(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 35
        self._speed = 4

    def special(self, target):
        self._power = 42
        self._speed = 7
        target.setHealth(target.getHealth() - self._power)

class Support(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._health = 500
        self._armor = 8
        self._speed = 4

    def special(self, target):
        self._speed = 6
        target.setHealth(target.getHealth() + 150)

warrior = Warrior("bambang", pos_x=10)
assassin = Assassin("joko", pos_x=25)
support = Support("udin", pos_x=30)

print("health (before)", warrior.getHealth())
assassin.attack(warrior)

print("health (after)", warrior.getHealth())
print("-"*10)

print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ",support.getSpeed())

support.special(warrior)

print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ",support.getSpeed())




        



        
    


