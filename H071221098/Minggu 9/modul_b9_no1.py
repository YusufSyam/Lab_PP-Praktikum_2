from hero import Warrior, Assassin, Support

warrior = Warrior('bambang', pos_x=10)
assassin = Assassin ('joko', pos_x=25)
support = Support ('udin', pos_x=30)
#sebelum
print("health (before)", warrior.getHealth())
assassin.attack(warrior)\
#sesudah
print("health (after)", warrior.getHealth())
print("-"*10)
#sebelum
print('Warrior (health)', warrior.getHealth())
print('Support (speed) : ',support.getSpeed())
#sesudah
print('Warrior (health)', warrior.getHealth())
print('Support (speed) : ', support.getSpeed())