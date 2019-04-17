# Создать класс Car. Атрибуты: марка, модель, год  выпуска,
# скорость(по умолчанию 0). Методы: увеличить скорости(скорость + 5),
# уменьшение скорости(скорость  - 5),
# стоп(сброс скорости на 0),
# отображение скорости, разворот(изменение знака скорости).
# Все атрибуты приватные.


class Car:
    def __init__(self, mark, model, year, speed):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__speed = speed

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def figure(self, mark):
        self.__mark = mark

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__year = speed

    def more_speed(self):
        self.__speed += 5
        return self.__speed

    def less_speed(self):
        self.__speed -= 5
        return self.__speed

    def stop_car(self):
        self.__speed = 0
        return self.__speed

    def return_car(self):
        if self.__speed < 0:
            self.__speed = abs(self.__speed)
        else:
            self.__speed = -self.__speed
        return self.__speed


def main():

    car = Car('BMW', '530d', '2018', 0)
    print(car.mark)
    print(car.model)
    print(car.year)
    print(car.speed)
    car.more_speed()
    print(car.speed)
    car.more_speed()
    print(car.speed)
    car.return_car()
    print(car.speed)
    car.more_speed()
    print(car.speed)
    car.stop_car()
    print(car.speed)

if __name__ == '__main__':
        main()
