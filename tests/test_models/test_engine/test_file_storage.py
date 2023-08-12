#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py"""
import os
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""
    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        bm = BaseModel()
        models.storage.new(bm)

        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())

    def test_save(self):
        bm = BaseModel()

        models.storage.new(bm)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)

    def test_reload(self):
        bm = BaseModel()

        models.storage.new(bm)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)


if __name__ == "__main__":
    unittest.main()
