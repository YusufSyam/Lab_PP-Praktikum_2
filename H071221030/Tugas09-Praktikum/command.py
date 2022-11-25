from hero import Warrior, Assassin, Support

warrior = Warrior("Bambang", 10)
assassin = Assassin("Joko", 25)
support = Support("Udin", 30)

print("health (before)", warrior.getHealth())
assassin.attack(warrior)

print("health (after)", warrior.getHealth())

print("-"*10)

print("Warrior (health)", warrior.getHealth())
print("Support (speed)", support.getSpeed())

support.special(warrior)

print("Warrior (health)", warrior.getHealth())
print("Support (speed)", support.getSpeed())