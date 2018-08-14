import unittest
from calculator import calculator

class test_calculator (unittest.TestCase):
    def setUp(self):
        self.helper = calculator()
        self.planets = [
            {"name": "Prueba1", "speed":  1, "ratio": 500},
            {"name": "Prueba2", "speed":  3, "ratio": 2000},
            {"name": "Prueba3", "speed": -5, "ratio": 1000},
        ]
        self.planets_db = [
            ["Prueba1",  1, 500],
            ["Prueba2",  3, 2000],
            ["Prueba3", -5, 1000],
        ]

    def test_planets_handle(self):
        self.helper.set_planets(self.planets)
        self.assertEqual(self.helper.get_planets(), self.planets)

    def test_load_planets(self):
        self.assertEqual(self.helper.load_planets(self.planets_db), self.planets)

    def test_day_weather(self):
        self.assertEqual(self.helper.day_weather(self.planets, 0), "Sequia")
        self.assertEqual(self.helper.day_weather(self.planets, 5), "Indeterminado")
        self.assertEqual(self.helper.day_weather(self.planets, 47), "Presion y Temperatura Optima")
        self.assertEqual(self.helper.day_weather(self.planets, 72), "Lluvia Intensa")
        self.assertEqual(self.helper.day_weather(self.planets, 23), "Lluvia")

if __name__ == '__main__':
    unittest.main()