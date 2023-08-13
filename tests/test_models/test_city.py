#!user/bin/python3
import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.city import City


class TestCity(TestBaseModel):
    def setUp(self):
        self.model = City()

    def tearDown(self):
        del self.model


if __name__ == "__main__":
    unittest.main()
