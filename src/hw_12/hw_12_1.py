# Добавить в класс Pet пустой метод voice.
# Заменить имена методов bark, meow на voice.
# Создать функцию, принимающая список животных
# и вызывающая у каждого животного метод voice.

from my_classes import (
    Cat,
    Dog,
)


def pets(args):
    for pet in args:
        pet.voice()


def main():
    args = [Cat("Ilya", 12, "Max", 70, 3000), Dog("Fridrih", 5, "Liza", 50, 1500)]

    pets(args)


if __name__ == '__main__':
        main()
