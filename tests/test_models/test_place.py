#!/usr/bin/python3
""" Tests class Place """
import unittest
from models.place import Place
from models.base_model import BaseModel
import os
import pep8


class TestPlace(unittest.TestCase):
    """ Tests different attributes and functionality of Place class """

    @classmethod
    def setup_class(cls):
        """ Sets up an instance of Place """
        cls.place = Place()
        cls.place.city_id = "Han"
        cls.place.user_id = "Mulan"
        cls.place.name = "Great Wall"
        cls.place.description = "Tranquil as a forest"
        cls.place.number_rooms = 0
        cls.place.number_bathrooms = 0
        cls.place.max_guest = 0
        cls.place.price_by_night = 0
        cls.place.latitude = 0.0
        cls.place.longitude = 0.0
        cls.place.amenity_ids = []

    @classmethod
    def teardown_class(cls):
        """ Deletes instance and attempts to remove file if it exists """
        del cls.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """ Tests if script meets PEP8 styling """
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "Fails PEP8")

    def test_functions(self):
        """ Tests for methods inside Amenity class """
        self.assertIsNotNone(Place.__doc__)

    def test_subclass(self):
        """ Tests if instance is a subclass of BaseModel """
        self.setup_class()
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_save(self):
        """ Tests for funcionality of save method """
        self.setup_class()
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

if __name__ == '__main__':
    unittest.main()
