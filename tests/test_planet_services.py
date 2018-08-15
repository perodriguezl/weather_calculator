import unittest
from services.planet_services import planet_services
from models.planet import planet

class test_planet_services (unittest.TestCase):
    def setUp(self):
        self.helper = planet_services(mock_db_connector(), planet)

    def test_clean_repositoy(self):
        self.assertIsNone(self.helper.clean_repository())

    def test_set_persist(self):
        self.assertIsNone(self.helper.set_persist(True))
        self.assertIsNone(self.helper.set_persist(False))

    def test_get_planets(self):
        planet = self.helper.get_planets()[0]
        self.assertEqual(planet.get_name(), "Prueba")
        self.assertEqual(planet.get_speed(), 1)
        self.assertEqual(planet.get_ratio(), 2)

    def test_add_day(self):
        planet = self.helper.add_day(10, "Prueba")
        self.assertIsNone(planet)

    def test_handle_persist(self):
        self.helper.set_persist(True)
        self.assertTrue(self.helper.get_persist)

class mock_db_connector():

    def connection(self):
        pass

    def query(self, sql):
        if sql == "SELECT * FROM planets":
            return [["Prueba", 1, 2]]
        pass
