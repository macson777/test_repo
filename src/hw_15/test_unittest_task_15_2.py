import unittest
from hw_15.task_15_2 import Circle, Triangle, Square


class CalcTest(unittest.TestCase):

    def setUp(self):
        self.circle = Circle(1, 1, 4)
        self.triangle = Triangle(0, 0, 8, 2, -2, 6)
        self.square = Square(1, 5, 8, 3)

    def test_calc_perimetr_and_s_circle(self):
        result = self.circle.perimetr_s_okr()
        self.assertEqual(result, (25.12, 50.24))

    def test_calc_perimetr_and_s_triangle(self):
        result = self.triangle.perimetr_s_triangle()
        self.assertEqual(result, (25.34109618584109, 26.000000000000007))

    def test_calc_perimetr_and_s_square(self):
        result = self.square.perimetr_s_square()
        self.assertEqual(result, (20.591260281974, 26.5))

