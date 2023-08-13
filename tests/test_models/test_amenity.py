#!user/bin/python3
import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


class TestAmenity(TestBaseModel):
    def setUp(self):
        self.model = Amenity()

    def tearDown(self):
        del self.model


if __name__ == "__main__":
    unittest.main()
