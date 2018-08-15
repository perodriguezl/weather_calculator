import unittest
from services.model_services import db_connector

class test_db_connector (unittest.TestCase):
    def setUp(self):
        self.helper = db_connector()

    def test_set_db_route(self):
        self.helper.set_db_route("test")
        self.assertEqual(self.helper.db_route, "test")

    def test_get_db_route(self):
        self.helper.db_route = "test"
        self.assertEqual(self.helper.get_db_route(), "test")

    def test_connection(self):
        self.assertRaises(NotImplementedError, lambda: self.helper.connection())

    def test_query(self):
        self.assertRaises(NotImplementedError, lambda: self.helper.query("anything"))