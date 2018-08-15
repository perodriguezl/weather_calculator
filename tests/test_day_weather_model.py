import unittest
from models.day_weather import day_weather

class test_day_weather_model (unittest.TestCase):
    def setUp(self):
        self.helper = day_weather(1, "Sequia")

    def test_get_day(self):
        self.assertTrue(self.helper.get_day(), 1)

    def test_get_weather(self):
        self.assertTrue(self.helper.get_weather(), "Sequia")

    def test_set_day(self):
        self.helper.set_day(5)
        self.assertTrue(self.helper.day, 5)

    def test_set_weather(self):
        self.helper.set_weather("Lluvia")
        self.assertTrue(self.helper.weather, "Lluvia")