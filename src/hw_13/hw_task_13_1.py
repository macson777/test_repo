from my_classes import (
    Pet,
    Cat,
    Dog,
    Parrot,
)


def main():
    cat = Cat("Fridrih", 5, "Liza", 50, 1500)
    print(cat.name)
    print(cat.master)
    cat.meow()
    cat.birthday()
    print(cat.age)

    dog = Dog("Ilya", 12, "Max", 70, 3000)
    print(dog.name)
    print(dog.master)
    dog.bark()
    dog.birthday()
    dog.birthday()
    dog.birthday()
    dog.birthday()
    dog.birthday()
    print(dog.age)
    dog.is_alive
    dog.change_weight()
    print(dog.weight)

    parrot = Parrot("Kesha", 3, "Bob", 10, 200, 'orange')
    print(parrot.name)
    print(parrot.master)
    parrot.fly()
    parrot.birthday()
    parrot.change_weight()
    print(parrot.weight)
    print(parrot.age)
    parrot.fly()
    print(parrot.species)
    print(Pet.get_counter())
    print(Pet.get_random_name())


if __name__ == '__main__':
    main()

