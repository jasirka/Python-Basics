
# The @abstractmethod decorator is used to mark sound() as an abstract method. 
# This means any subclass must implement this method to be instantiated.
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

dog = Dog()
print(dog.sound())

animal = Animal()  # TypeError: Can't instantiate abstract class Animal without an implementation 
animal.sound()     # for abstract method 'sound'
        