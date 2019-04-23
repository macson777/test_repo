class Pet:
    def __init__(self, name, age, master, height, weight):
        self.name = name
        self.age = age
        self.master = master
        self.height = height
        self.weight = weight
        self.is_alive = True


    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')

    def birthday(self):
        self.age += 1

    def change_weight(self, weight=None):
        if weight:
            self.weight += weight
        else:
            self.weight += 200

    def change_height(self, height=None):
        if height:
            self.height += height
        else:
            self.height += 200



class Dog(Pet):
    def voice(self):
        print('Woof Woof!')

    def birthday(self):
        if self.is_alive:
            super().birthday()
        if self.age > 13:
            self.is_alive = False


class Cat(Pet):
    def voice(self):
        print('Meow Meow!')

    def birthday(self):
        if self.is_alive:
            super().birthday()
        if self.age > 16:
            self.is_alive = False


class Parrot(Pet):
    def __init__(self, name, age, master, height, weight, species):
        super().__init__(name, age, master, height, weight)
        self.species = species

    def birthday(self):
        if self.is_alive:
            super().birthday()
            if self.age > 60:
                self.is_alive = False

    def change_weight(self, weight=None):
        if weight:
            self.weight += weight
        else:
            self.weight += 50

    def change_height(self, height=None):
        if height:
            self.height += height
        else:
            self.height += 5

    def fly(self):
        if self.weight > 500:
            print('This parrot can not Fly!')
        else:
            print('Fly!')


