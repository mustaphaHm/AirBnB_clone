#!user/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    def test_initialization(self):
        instance = User()
        self.assertTrue(instance.id)
        self.assertIsInstance(instance.id, str)
        self.assertRegex(instance.id,
                         r'^[0-9a-f]{8}-[0-9a-f]{4}-'
                         r'[4][0-9a-f]{3}-[89ab][0-9a-f]{3}-'
                         r'[0-9a-f]{12}$')
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertEqual(instance.email, "")
        self.assertEqual(instance.password, "")
        self.assertEqual(instance.first_name, "")
        self.assertEqual(instance.last_name, "")

    def test_save_method(self):
        instance = User()
        init_updated_at = instance.updated_at
        instance.save()
        new_updated_at = instance.updated_at
        self.assertNotEqual(init_updated_at, new_updated_at)

    def test_to_dict_method(self):
        instance = User()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertIn('__class__', instance_dict)
        self.assertIn('id', instance_dict)
        self.assertIn('created_at', instance_dict)
        self.assertIn('updated_at', instance_dict)
        self.assertIn('email', instance_dict)
        self.assertIn('password', instance_dict)
        self.assertIn('first_name', instance_dict)
        self.assertIn('last_name', instance_dict)
        self.assertEqual(instance_dict['__class__'], 'User')


if __name__ == "__main__":
    unittest.main()
