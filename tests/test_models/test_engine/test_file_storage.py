import os
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""
    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        bm = BaseModel()
        models.storage.new(bm)
        user = User()
        models.storage.new(user)
        state = State()
        models.storage.new(state)
        city = City()
        models.storage.new(city)
        amenity = Amenity()
        models.storage.new(amenity)
        place = Place()
        models.storage.new(place)
        review = Review()
        models.storage.new(review)

        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + user.id, models.storage.all().keys())
        self.assertIn(user, models.storage.all().values())
        self.assertIn("State." + state.id, models.storage.all().keys())
        self.assertIn(state, models.storage.all().values())
        self.assertIn("City." + city.id, models.storage.all().keys())
        self.assertIn(city, models.storage.all().values())
        self.assertIn("Amenity." + amenity.id, models.storage.all().keys())
        self.assertIn(amenity, models.storage.all().values())
        self.assertIn("Place." + place.id, models.storage.all().keys())
        self.assertIn(place, models.storage.all().values())
        self.assertIn("Review." + review.id, models.storage.all().keys())
        self.assertIn(review, models.storage.all().values())

    def test_save(self):
        bm = BaseModel()
        models.storage.new(bm)
        user = User()
        models.storage.new(user)
        state = State()
        models.storage.new(state)
        city = City()
        models.storage.new(city)
        amenity = Amenity()
        models.storage.new(amenity)
        place = Place()
        models.storage.new(place)
        review = Review()
        models.storage.new(review)

        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + user.id, save_text)
            self.assertIn("State." + state.id, save_text)
            self.assertIn("City." + city.id, save_text)
            self.assertIn("Amenity." + amenity.id, save_text)
            self.assertIn("Place." + place.id, save_text)
            self.assertIn("Review." + review.id, save_text)

    def test_reload(self):
        bm = BaseModel()
        models.storage.new(bm)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)

        user = User()
        models.storage.new(user)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("User." + user.id, objs)

        state = State()
        models.storage.new(state)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("State." + state.id, objs)

        city = City()
        models.storage.new(city)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("City." + city.id, objs)

        amenity = Amenity()
        models.storage.new(amenity)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("Amenity." + amenity.id, objs)

        place = Place()
        models.storage.new(place)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("Place." + place.id, objs)

        review = Review()
        models.storage.new(review)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("Review." + review.id, objs)


if __name__ == "__main__":
    unittest.main()
