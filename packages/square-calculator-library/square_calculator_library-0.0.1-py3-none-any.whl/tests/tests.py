import sys

sys.path.append('..')

import unittest

from square_calculator_library.square_calculator import constants
from square_calculator_library.square_calculator import square


class TestSquareCalculator(unittest.TestCase):

    def test_ability_transmit_only_positive_numbers(self):
        values_results = (
            # если встречаются отрицательные значения
            # при передаче одного параметра
            ({'a': -500}, ValueError),
            # при передаче двух параметров
            ({'a': 1, 'b': -500}, ValueError),
            # при передаче трёх параметров
            ({'a': 1, 'b': -500, 'c': 50}, ValueError),
            # при передаче четырёх параметров
            ({'a': 1, 'b': -500, 'c': 50, 'd': -10}, ValueError),
            # если встречаются нулевые значения
            # при передаче одного параметра
            ({'a': 0}, ValueError),
            # при передаче двух параметров
            ({'a': 0, 'b': -500}, ValueError),
            # при передаче трёх параметров
            ({'a': 0, 'b': -500, 'c': 50}, ValueError),
            # при передаче четырёх параметров
            ({'a': 0, 'b': -500, 'c': 50, 'd': -10}, ValueError),
        )
        for value, expected_error in values_results:
            with self.subTest():
                with self.assertRaises(expected_error):
                    sq = square.Square(**value)
                    sq.calculate()

    def test_square_calculating(self):
        def verification_triangle_square(*args):
            half_perimeter = sum(args) / 2
            return (
                half_perimeter
                * (half_perimeter - args[0])
                * (half_perimeter - args[1])
                * (half_perimeter - args[2])
            ) ** 0.5

        def varification_circle_square(radius):
            return constants.PI * radius ** 2

        def varification_ellipse_square(a, b):
            return constants.PI * a * b

        def varification_rectangle_square(a, b):
            return a * b

        def varification_trapezoid_square(a, b, h):
            return 0.5 * (a + b) * h

        values_results = (
            # при передаче одного параметра - окружность
            ({'a': 10}, varification_circle_square(10)),
            # при передаче двух параметров для элипса
            (
                {'a': 10, 'b': 500, 'figure_type': constants.FIGURE_TYPES[1]},
                varification_ellipse_square(10, 500)
            ),
            # при передаче двух параметров для прямоугольника
            (
                {'a': 10, 'b': 500, 'figure_type': constants.FIGURE_TYPES[2]},
                varification_rectangle_square(10, 500)
            ),
            # при передаче двух параметров и высоты для трапеции
            (
                {
                    'a': 10, 'b': 500, 'h': 50,
                    'figure_type': constants.FIGURE_TYPES[4]
                },
                varification_trapezoid_square(10, 500, 50)
            ),
            # при передаче трёх параметров для треугольника
            (
                {'a': 10, 'b': 500, 'с': 50},
                verification_triangle_square(10, 500, 50)
            ),
        )
        for value, expected_result in values_results:
            with self.subTest(
                value=value,
                expected_result=expected_result,
                msg=(
                    f'При передаче значений {value},\n'
                    f'результат отличался от ожидаемого: {expected_result}.'
                )
            ):
                values = {
                    index: v for index, v in value.items()
                    if index not in [
                        'figure_type',
                        'h'
                    ]
                }
                sq = square.Square(**values)
                if any(attr == 'figure_type' for attr in value.keys()):
                    sq.figure_type = value['figure_type']
                if any(attr == 'h' for attr in value.keys()):
                    sq.trapezoid_h = value['h']
                result = sq.calculate()

                self.assertEqual(result, expected_result)

    def test_figure_type_definitions(self):
        values_results = (
            # при передаче одного параметра - окружность
            ({'a': 10}, constants.FIGURE_TYPES[0]),
            # при передаче двух параметров для элипса
            (
                {'a': 10, 'b': 500, 'figure_type': constants.FIGURE_TYPES[1]},
                constants.FIGURE_TYPES[1]
            ),
            # при передаче двух параметров для прямоугольника
            (
                {'a': 10, 'b': 500, 'figure_type': constants.FIGURE_TYPES[2]},
                constants.FIGURE_TYPES[2]
            ),
            # при передаче двух параметров и высоты для трапеции
            (
                {
                    'a': 10, 'b': 500, 'h': 50,
                    'figure_type': constants.FIGURE_TYPES[4]
                },
                constants.FIGURE_TYPES[4]
            ),
            # при передаче трёх параметров для треугольника
            (
                {'a': 10, 'b': 500, 'с': 50},
                constants.FIGURE_TYPES[5]
            ),
            # при передаче трёх параметров для прямоугольного треугольника
            (
                {'a': 3, 'b': 4, 'с': 5},
                constants.FIGURE_TYPES[3]
            ),
        )
        for value, expected_result in values_results:
            with self.subTest(
                value=value,
                expected_result=expected_result,
                msg=(
                    f'При передаче значений {value},\n'
                    f'результат отличался от ожидаемого: {expected_result}.'
                )
            ):
                values = {
                    index: v for index, v in value.items()
                    if index not in [
                        'figure_type',
                        'h'
                    ]
                }
                sq = square.Square(**values)
                if any(attr == 'figure_type' for attr in value.keys()):
                    sq.figure_type = value['figure_type']
                if any(attr == 'h' for attr in value.keys()):
                    sq.trapezoid_h = value['h']
                sq.calculate()
                result = sq.figure_type

                self.assertEqual(result, expected_result)

    def test_assert_for_not_circle_or_triangle_without_figure_type(self):
        values_results = (
            # без передачи параметров
            ({}, Exception),
            # при передаче двух параметров
            ({'a': 1, 'b': 500}, Exception),
            # при передаче четырёх параметров
            ({'a': 1, 'b': 500, 'c': 50, 'd': 10}, Exception),
        )
        for value, expected_error in values_results:
            with self.subTest():
                with self.assertRaises(expected_error):
                    sq = square.Square(**value)
                    sq.calculate()


unittest.main()
