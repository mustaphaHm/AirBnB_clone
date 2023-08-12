# !/usr/bin/python3
"""Implementing UnitTests."""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Definition of class TestBaseModel."""

    def test_initialization(self):
        instance = BaseModel()
        """Test if Id is Valid UUID."""
        self.assertTrue(instance.id)
        self.assertIsInstance(instance.id, str)
        self.assertRegex(instance.id,
                         r'^[0-9a-f]{8}-[0-9a-f]{4}-'
                         r'[4][0-9a-f]{3}-[89ab][0-9a-f]{3}-'
                         r'[0-9a-f]{12}$')
        """Test if created_at and updated_at are instances of datetime."""
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_save_method(self):
        instance = BaseModel()
        """Test if updated_at get updated."""
        init_updated_at = instance.updated_at
        instance.save()
        new_updated_at = instance.updated_at
        self.assertNotEqual(init_updated_at, new_updated_at)

    def test_to_dict_method(self):
        instance = BaseModel()
        """Test the function to dict."""
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertIn('__class__', instance_dict)
        self.assertIn('id', instance_dict)
        self.assertIn('created_at', instance_dict)
        self.assertIn('updated_at', instance_dict)
        self.assertEqual(instance_dict['__class__'], 'BaseModel')

    if __name__ == "__main__":
        unittest.main()
