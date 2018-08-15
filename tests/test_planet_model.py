import unittest
from models.planet import planet

class test_planet_model (unittest.TestCase):
    def setUp(self):
        self.helper = planet("Prueba", 1, 2)

    def test_get_name(self):
        self.assertTrue(self.helper.get_name(), "Prueba")

    def test_get_speed(self):
        self.assertTrue(self.helper.get_speed(), 1)

    def test_get_ratio(self):
        self.assertTrue(self.helper.get_ratio(), 2)

    def test_set_name(self):
        self.helper.set_name("Nueva")
        self.assertTrue(self.helper.name, "Nueva")

    def test_set_speed(self):
        self.helper.set_speed(5)
        self.assertTrue(self.helper.speed, 5)

    def test_set_ratio(self):
        self.helper.set_ratio(20)
        self.assertTrue(self.helper.ratio, 20)