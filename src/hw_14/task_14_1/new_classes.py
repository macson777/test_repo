from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    @abstractmethod
    def voice(self):
        pass

class FelineInterface(Animal):
    @abstractmethod
    def scratch(self):
        print("scratching")


class CanineInterface(Animal):
    @abstractmethod
    def swim(self):
        print("swimming")

class Pet(Animal):
    pass


class WildAnimal(Animal):
    pass

class Dog(Pet, CanineInterface):
    def voice(self):
        print('Gav Gav')

    def swim(self):
        print("swimming")

class Cat(Pet, FelineInterface):
    def voice(self):
        print('Meow Meow!')

    def scratch(self):
        print("scratching")

class Lion(WildAnimal, FelineInterface):
    def voice(self):
        print('Arrrrrrrr')

    def scratch(self):
        print("scratching")

class Wolf(WildAnimal, CanineInterface):
    def voice(self):
        print('Woof Woof')

    def swim(self):
        print("swimming")



