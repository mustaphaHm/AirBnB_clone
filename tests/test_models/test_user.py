#!user/bin/python3
import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.user import User


class TestPlace(TestBaseModel):
    def setUp(self):
        self.model = User()

    def tearDown(self):
        del self.model


if __name__ == "__main__":
    unittest.main()
