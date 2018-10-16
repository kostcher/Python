# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return math.sqrt(
            (self.p2[0] - self.p1[0]) ** 2 + (self.p2[1] - self.p1[1]) ** 2
        )


class Triangle:
    def __init__(self, points):
        self.a = Line(points[0], points[1])
        self.b = Line(points[1], points[2])
        self.c = Line(points[2], points[0])

    def get_perimeter(self):
        return self.a.length() + self.b.length() + self.c.length()

    def get_square(self):
        hp = self.get_perimeter() * 0.5

        return math.sqrt(
            hp * (hp - self.a.length()) * (hp - self.b.length()) * (hp - self.c.length())
        )

    def get_height(self):
        square = self.get_square();
        return {
            'a': square / 0.5 * self.a.length(),
            'b': square / 0.5 * self.b.length(),
            'c': square / 0.5 * self.c.length(),
        }


points = [[3, 2], [7, 5], [0, 0]]

triangle = Triangle(points)

print(triangle.get_perimeter())
print(triangle.get_square())
print(triangle.get_height())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
