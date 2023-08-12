#!user/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    def test_initialization(self):
        instance = Review()
        self.assertTrue(instance.id)
        self.assertIsInstance(instance.id, str)
        self.assertRegex(instance.id,
                         r'^[0-9a-f]{8}-[0-9a-f]{4}-'
                         r'[4][0-9a-f]{3}-[89ab][0-9a-f]{3}-'
                         r'[0-9a-f]{12}$')
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertEqual(instance.place_id, "")
        self.assertEqual(instance.user_id, "")
        self.assertEqual(instance.text, "")

    def test_save_method(self):
        instance = Review()
        init_updated_at = instance.updated_at
        instance.save()
        new_updated_at = instance.updated_at
        self.assertNotEqual(init_updated_at, new_updated_at)

    def test_to_dict_method(self):
        instance = Review()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertIn('__class__', instance_dict)
        self.assertIn('id', instance_dict)
        self.assertIn('created_at', instance_dict)
        self.assertIn('updated_at', instance_dict)
        self.assertIn('place_id', instance_dict)
        self.assertIn('user_id', instance_dict)
        self.assertIn('text', instance_dict)
        self.assertEqual(instance_dict['__class__'], 'Review')


if __name__ == "__main__":
    unittest.main()