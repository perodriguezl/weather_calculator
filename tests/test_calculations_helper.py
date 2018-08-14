import unittest
from calculations_helper import calculations_helper

class test_calculations_helper (unittest.TestCase):
    def setUp(self):
        self.helper = calculations_helper()

    def test_aligned_planets(self):
        self.assertTrue(self.helper.aligned_planets(45, 225))
        self.assertTrue(self.helper.aligned_planets(90, 270))
        self.assertFalse(self.helper.aligned_planets(125, 270))

    def test_position_calculator_degrees(self):
        self.assertEqual(self.helper.position_calculator_degrees(1, 1), 1)
        self.assertEqual(self.helper.position_calculator_degrees(-5, 1), 355)
        self.assertEqual(self.helper.position_calculator_degrees(-5, 10), 310)

    def test_calculate_side(self):
        planet_1 = {'x': 1, 'y': 2}
        planet_2 = {'x': 0, 'y': 2}
        self.assertEqual(self.helper.calculate_side(planet_1, planet_2), 1)

    def test_calculate_perimeter(self):
        planets = [
            {'x': 0, 'y': 0},
            {'x': 0, 'y': 1},
            {'x': 1, 'y': 0}
        ]
        result = self.helper.calculate_perimeter(planets)
        self.assertEqual(result['perimeter'], 3.414213562373095)

    def test_calculate_area(self):
        planets = [
            {'ratio': 500, 'speed': 1},
            {'ratio': 2000, 'speed': 3},
            {'ratio': 1000, 'speed': -5}
        ]
        self.assertEqual(self.helper.calculate_area([1, 1, 1.41]), 0.24999114937500017)

    def test_calculate_x(self):
        planet = {'ratio': 5000, 'position': 0}
        self.assertEqual(self.helper.calculate_x(planet), 5000)

    def test_calculate_x(self):
        planet = {'ratio': 5000, 'position': 90}
        self.assertEqual(self.helper.calculate_x(planet), 0)

    def test_position_calculator_degrees(self):
        self.assertEqual(self.helper.position_calculator_degrees(1, 5), 5)

    def test_is_set_included(self):
        self.assertTrue(self.helper.is_sun_included([359, 5, 180]))
        self.assertTrue(self.helper.is_sun_included([1, 5, 182]))
        self.assertFalse(self.helper.is_sun_included([1, 5, 90]))
        self.assertFalse(self.helper.is_sun_included([1, 45, 90]))


if __name__ == '__main__':
    unittest.main()