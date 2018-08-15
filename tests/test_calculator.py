import unittest
from calculator import calculator
from models.planet import planet

class test_calculator (unittest.TestCase):
    def setUp(self):
        self.helper = calculator()
        self.planets = [
            {"name": "Prueba1", "speed":  1, "ratio": 500},
            {"name": "Prueba2", "speed":  3, "ratio": 2000},
            {"name": "Prueba3", "speed": -5, "ratio": 1000},
        ]
        self.planets_db = [
            planet("Prueba1",  1, 500),
            planet("Prueba2",  3, 2000),
            planet("Prueba3", -5, 1000)
        ]

    def test_planets_handle(self):
        self.helper.set_planets(self.planets)
        self.assertEqual(self.helper.get_planets(), self.planets)

    def test_load_planets(self):
        self.assertEqual(self.helper.load_planets(self.planets_db), self.planets)

    def test_day_weather_calculation(self):
        self.assertEqual(self.helper.day_weather_calculation(self.planets, 0), "Sequia")
        self.assertEqual(self.helper.day_weather_calculation(self.planets, 5), "Indeterminado")
        self.assertEqual(self.helper.day_weather_calculation(self.planets, 47), "Presion y Temperatura Optima")
        self.assertEqual(self.helper.day_weather_calculation(self.planets, 72), "Lluvia Intensa")
        self.assertEqual(self.helper.day_weather_calculation(self.planets, 23), "Lluvia")

    def test_would_persist(self):
        arguments = ['uno.py', 'populate']
        self.assertTrue(self.helper.would_persist(arguments))
        arguments = ['uno.py']
        self.assertFalse(self.helper.would_persist(arguments))
        arguments = ['uno.py', '']
        self.assertFalse(self.helper.would_persist(arguments))


    def test_calculate_weather(self):
        self.assertEqual(self.helper.calculate_weather(self.planets, 0, 0), [])
        self.assertEqual(self.helper.calculate_weather(self.planets, 0, 1)[0].get_weather(), "Sequia")
        self.assertEqual(len(self.helper.calculate_weather(self.planets, 0, 1)), 1)


    def test_show_results(self):
        self.assertIsNone(self.helper.show_results())

if __name__ == '__main__':
    unittest.main()