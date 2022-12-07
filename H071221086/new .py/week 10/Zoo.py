from abc import ABC, abstractmethod

#class abstract
class Animal(ABC):
    @abstractmethod
    def suara(self):
        pass
#polymorphism
    def __init__(self, nama):
        self.nama = nama

#Inharitance Hewan(Animal)
class Hewan(Animal):
    def __init__(self, nama):
        super().__init__(nama)
        #Encapsulation (_)
        self._suara = "Suara"
    
    #Polymorphism
    def serang(self,target):
        #Encapsulation (_)
        target._health -= self._power
    #Polymorphism
    def bergerak(self):
        print("Bergerak dengan cara")
    #Polymorphism
    def bertarung(self):
        print("Bertarung dengan")
   
#Inharitance
class Kucing(Hewan):
    def __init__(self, nama):
        super().__init__(nama)
        #Encapsulation (_)
        self._health = 200
        #Encapsulation (_)
        self._power = 100
    #Polymorphism
    def cekDarah(self):
        #Encapsulation (_)
        print(self._health)
    #Polymorphism
    def serang(self,target):
        #Encapsulation (_)
        target._health -= self._power
    #Polymorphism
    def bergerak(self):
        print("Kucing bergerak dengan menggunakan kaki dan tangannya")
    #Polymorphism
    def bertarung(self):
        print("Kucing bertarung dengan mengunakan cakarnya")
    #Polymorphism
    def suara(self):
        print("Meow")
#Inharitance    
class Anjing(Hewan):
    def __init__(self, nama):
        super().__init__(nama)
        #Encapsulation (_)
        self._health = 250
        #Encapsulation (_)
        self._power = 50
    #Polymorphism
    def cekDarah(self):
        #Encapsulation (_)
        print(self._health)    
    #Polymorphism
    def serang(self,target):
        #Encapsulation (_)
        target._health -= self._power
    #Polymorphism
    def bergerak(self):
        print("Anjing bergerak dengan menggunakan kaki dan tangannya")
    #Polymorphism
    def bertarung(self):
        print("Anjing bertarung menggunakan taringnya")
    #Polymorphism
    def suara(self):
        print("Guk-guk")
       
        