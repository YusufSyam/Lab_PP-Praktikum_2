class Human:
    def __init__(self,name,pos_x):
        self.nama=name
        self._position=pos_x
    
    def setMovement(self,set):
        set=set.upper()
        if set=='L':
            self._position-=self.speed
        if set=='R':
            self._position+=self.speed

    def getMovement(self):
        return self._position


class Hero(Human):
    def __init__(self,name,pos_x):
        super().__init__(name,pos_x)
        self._power=15
        self._health=400
        self._armor=15
        self._speed=3

    def attack(self,target):
        target.setHealth(target.getHealth()-self._power)

    def setPower(self,power):
        self._power=power

    def getPower(self):
        return self._power

    def setHealth(self,health):
        self._health=health

    def getHealth(self):
        return self._health

    def setArmor(self,armor):
        self._armor=armor

    def getArmor(self):
        return self._armor

    def setSpeed(self,speed):
        self._speed=speed

    def getSpeed(self):
        return self._speed


class Warrior(Hero):
    def __init__(self,name,pos_x):
        super().__init__(name,pos_x)
        self._power=26
        self._armor=30
    
    def special(self, target):
        self._armor=45
        self._power=32
        target.setHealth(target.getHealth()-self._power)


class Assassin(Hero):
    def __init__(self,name,pos_x):
       super().__init__(name,pos_x)
       self._power=35
       self._speed=4

    def special(self, target):
        self._speed=7
        self._power=42
        target.setHealth(target.getHealth()-self._power)


class Support(Hero):
    def __init__(self,name,pos_x):
        super().__init__(name,pos_x)
        self._health=500
        self._armor=8
        self._speed=4

    def special(self, target):
        self._speed=6
        target.setHealth(target.getHealth()+150)


warrior = Warrior("bambang", pos_x=10)
assassin = Assassin("joko", pos_x=25)
support = Support ("udin", pos_x=30)

#sebelum
print("health (before)", warrior.getHealth())
assassin.attack(warrior)
#sesudah
print("health (after)", warrior.getHealth())

print("_"*10)

#sebelum
print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ", support.getSpeed())

support.special(warrior)

#sesudah
print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ", support.getSpeed())
