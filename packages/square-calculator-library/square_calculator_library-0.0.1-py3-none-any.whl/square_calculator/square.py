from . import constants as c
from . import exception_messages as m


class Square:
    """
    Рассчитывает площадь геометрической фигуры.
    По умолчанию рассчитывает площадь
    треугольника по трем сторонам
    или окружности по радиусу.

    Для корректной работы библиотеки
    при создании объекта класса
    необходимо передавать именованые аргументы,
    имена могут быть произвольными.

    Так нельзя:

    sq = Square(3, 4, 5)

    Так можно:

    sq = Square(a=3, b=4, c=5)

    Если передать в аргументах тип фигуры:
    'ellipse', 'rectangle' или 'trapezoid'
    рассчитывает площадь соответственно
    элипса, прямоугольника или трапеции.

    Тип фигур можно задавать,
    используя кортеж FIGURE_TYPES из файла constants.

    Определить тип рассчитаной фигуры можно через атрибут figure_type,
    например, так:

    sq = Square(a=3, b=4, c=5)

    print(sq.figure_type)

    >> 'rectangular triangle'
    """

    figure_type = None
    trapezoid_h = None

    def __init__(self, **kwargs):
        if self.validate(**kwargs):
            self.__dict__.update(kwargs)

    def validate(self, **kwargs):
        if any(i <= 0 for i in kwargs.values() if type(i) is int):
            raise ValueError('Длины всех сторон должны быть больше 0.')
        else:
            return True

    def get_attributes(self):
        return [
            value for index, value in self.__dict__.items() if index not in [
                'figure_type',
                'trapezoid_h'
            ]
        ]

    def count_attributes(self) -> int:
        return len(self.get_attributes())

    def is_rectangular(self) -> bool:
        """Вернет True, если стороны образуют прямоугольный треугольник."""
        sides = self.get_attributes()
        results = []
        for i, side in enumerate(sides):
            other_indexes = [
                index for index, value in enumerate(sides) if index != i
            ]
            if side ** 2 == (
                sides[other_indexes[0]] ** 2 + sides[other_indexes[1]] ** 2
            ):
                results.append(True)
            else:
                results.append(False)
        return any(results)

    def triangle(self):
        params = self.get_attributes()
        self.figure_type = c.FIGURE_TYPES[5]
        half_perimeter = sum(params) / 2
        return (
            half_perimeter
            * (half_perimeter - params[0])
            * (half_perimeter - params[1])
            * (half_perimeter - params[2])
        ) ** 0.5

    def rectangular_triangle(self):
        params = self.get_attributes()
        self.figure_type = 'rectangular triangle'
        exclude = max(params)
        katets = [side for side in params if side != exclude]
        return 0.5 * katets[0] * katets[1]

    def circle(self):
        self.figure_type = 'circle'
        return c.PI * self.get_attributes()[0] ** 2

    def ellipse(self):
        params = self.get_attributes()
        self.figure_type = 'ellipse'
        return c.PI * params[0] * params[1]

    def rectangle(self):
        params = self.get_attributes()
        self.figure_type = 'rectangle'
        return params[0] * params[1]

    def trapezoid(self):
        self.figure_type = 'trapezoid'
        return 0.5 * sum(self.get_attributes()) * self.trapezoid_h

    def calculate(self) -> float:
        attrs_count = self.count_attributes()
        if self.figure_type is None:
            if attrs_count not in [1, 3]:
                raise Exception(
                    m.ONE_OR_THREE_ARGS_REQUIRED
                )
            if attrs_count == 1:
                result = self.circle()
            if attrs_count == 3:
                if self.is_rectangular():
                    result = self.rectangular_triangle()
                else:
                    result = self.triangle()
        elif self.figure_type == c.FIGURE_TYPES[1]:
            if attrs_count == 2:
                result = self.ellipse()
            else:
                raise Exception(m.TWO_ARGS_REQUIRED)
        elif self.figure_type == c.FIGURE_TYPES[2]:
            if attrs_count == 2:
                result = self.rectangle()
            else:
                raise Exception(m.TWO_ARGS_REQUIRED)
        elif self.figure_type == c.FIGURE_TYPES[4]:
            if attrs_count == 2 and self.trapezoid_h is not None:
                result = self.trapezoid()
            else:
                raise Exception(m.TWO_ARGS_AND_TRAPEZOID_H_REQUIRED)
        else:
            raise Exception(m.UNKNOWN_ERROR)
        return result
