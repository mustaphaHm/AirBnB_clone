#!user/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_initialization(self):
        instance = Place()
        self.assertTrue(instance.id)
        self.assertIsInstance(instance.id, str)
        self.assertRegex(instance.id,
                         r'^[0-9a-f]{8}-[0-9a-f]{4}-'
                         r'[4][0-9a-f]{3}-[89ab][0-9a-f]{3}-'
                         r'[0-9a-f]{12}$')
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertEqual(instance.city_id, "")
        self.assertEqual(instance.user_id, "")
        self.assertEqual(instance.name, "")
        self.assertEqual(instance.description, "")
        self.assertEqual(instance.number_rooms, 0)
        self.assertEqual(instance.number_bathrooms, 0)
        self.assertEqual(instance.max_guest, 0)
        self.assertEqual(instance.price_by_night, 0)
        self.assertEqual(instance.latitude, 0.0)
        self.assertEqual(instance.longitude, 0.0)
        self.assertEqual(instance.amenity_ids, [])

    def test_save_method(self):
        instance = Place()
        init_updated_at = instance.updated_at
        instance.save()
        new_updated_at = instance.updated_at
        self.assertNotEqual(init_updated_at, new_updated_at)

    def test_to_dict_method(self):
        instance = Place()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertIn('__class__', instance_dict)
        self.assertIn('id', instance_dict)
        self.assertIn('created_at', instance_dict)
        self.assertIn('updated_at', instance_dict)
        self.assertIn('city_id', instance_dict)
        self.assertIn('user_id', instance_dict)
        self.assertIn('name', instance_dict)
        self.assertIn('description', instance_dict)
        self.assertIn('number_rooms', instance_dict)
        self.assertIn('number_bathrooms', instance_dict)
        self.assertIn('max_guest', instance_dict)
        self.assertIn('price_by_night', instance_dict)
        self.assertIn('latitude', instance_dict)
        self.assertIn('longitude', instance_dict)
        self.assertIn('amenity_ids', instance_dict)
        self.assertEqual(instance_dict['__class__'], 'Place')


if __name__ == "__main__":
    unittest.main()
