class Human :
    def __init__(self,name,pos_x) :
        self.nama = name
        self.__posisi = pos_x
        self._speed = 1

    def movement (self,arah) :
        for i in arah:
            if i == "L" :
                self.__posisi-=self._speed
            if i == "R" :
                self.__posisi+=self._speed

    def setPosition (self,pos_x) :
        self.__posisi = pos_x

    def getPosition (self) :
        return self.__posisi

    def setSpeed (self,speed) :
        self._speed = speed

    def getSpeed (self) :
        return self._speed

class Hero (Human):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    def attack (self,target) : #target itukan objek dari luar jadi untuk aksesnya itu harus pake setter getter
        target.setHealth((target.getHealth()-self._power))
    
    def setPower (self,power) :
        self._power = power

    def getPower (self) :
        return self._power

    def setHealth (self,health) :
        self._health = health

    def getHealth (self) :
        return self._health

    def setArmor (self,armor) :
        self._armor = armor

    def getArmor (self) :
        return self._armor

class Warrior (Hero) :
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 26
        self._armor = 30

    def special (self,target) :
        self._armor = 45
        self._power = 32
        self.attack(target)

class Assassin (Hero) :
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 35
        self._speed = 7

    def special (self,target) :
        self._power = 42
        self._speed = 7
        self.attack(target)
 
class Support (Hero) :
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._health = 500
        self._armor = 8
        self._speed = 4

    def special (self,target) :
        self._speed = 6
        target.setHealth((target.getHealth()+150))

warrior = Warrior("bambang", pos_x=10)
assassin = Assassin("joko", pos_x=25)
support = Support("udin",pos_x=30)

print("health (before)", warrior.getHealth())
assassin.attack(warrior)

print("health (after)", warrior.getHealth())
print("-"*10)

print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ",support.getSpeed())
support.special(warrior)

print("Warrior (health)", warrior.getHealth())
print("Support (speed): ",support.getSpeed())

print("-"*10)
print("Warrior (posisi)", warrior.getPosition())
print("Warrior (speed) : ",warrior.getSpeed())

print("-"*10)
warrior.movement ("r".upper())
print("Warrior (posisi)", warrior.getPosition())
print("Warrior (speed) : ",warrior.getSpeed())