import unittest
from services.day_weather_services import day_weather_services
from models.day_weather import day_weather

class test_day_weather_services (unittest.TestCase):
    def setUp(self):
        self.helper = day_weather_services(mock_db_connector(), day_weather)

    def test_get_day_wheater(self):
        result = self.helper.get_day_wheater(10)
        self.assertEqual(result.get_day(), 10)
        self.assertEqual(result.get_weather(), "Mock Weather")

class mock_db_connector():

    def connection(self):
        pass

    def query(self, sql):
        if sql == "SELECT * FROM day_weather WHERE day = 10":
            return [[10, "Mock Weather"]]
        pass
