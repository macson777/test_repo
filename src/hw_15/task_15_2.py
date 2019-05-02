class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure:
    pass


class Circle(Point):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def perimetr_s_okr(self):
        perimetr = 2 * 3.14 * self.r
        s_okr = 3.14 * (self.r ** 2)
        return perimetr, s_okr


class Triangle(Point):
    def __init__(self, x, y, x_1, y_1, x_2, y_2):
        super().__init__(x, y)
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2

    def perimetr_s_triangle(self):
        a_b = (((self.x_1 - self.x) ** 2) + ((self.y_1 - self.y) ** 2)) ** 0.5
        a_c = (((self.x_2 - self.x) ** 2) + ((self.y_2 - self.y) ** 2)) ** 0.5
        b_c = (((self.x_2 - self.x_1) ** 2) + ((self.y_2 - self.y_1) ** 2)) ** 0.5
        perimetr = a_b + b_c + a_c
        s_triangle = (0.5 * perimetr * ((0.5 * perimetr - a_b) * (0.5 * perimetr - b_c) * (0.5 * perimetr - a_c))) ** 0.5
        return perimetr, s_triangle


class Square(Point):
    def __init__(self, x, y, x_1, y_1):
        super().__init__(x, y)
        self.x_1 = x_1
        self.y_1 = y_1

    def perimetr_s_square(self):
        a_b = (((self.x_1 - self.x) ** 2) + ((self.y_1 - self.y) ** 2)) ** 0.5
        perimetr = 2 * 2 ** 0.5 * a_b
        s_square = (a_b ** 2) / 2
        return perimetr, s_square


def main():
    circle = Circle(1, 1, 4)
    print(circle.perimetr_s_okr())

    triangle = Triangle(0, 0, 8, 2, -2, 6)
    print(triangle.perimetr_s_triangle())

    square = Square(1, 5, 8, 3)
    print(square.perimetr_s_square())


if __name__ == '__main__':
        main()