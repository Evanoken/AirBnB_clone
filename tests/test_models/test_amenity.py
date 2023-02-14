#!/usr/bin/python3
""" Tests class Amenity """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import os
import pep8


class TestAmenity(unittest.TestCase):
    """ Tests different attributes and functionality of Amenity class """

    @classmethod
    def setup_class(cls):
        """ Sets up an instance of Amenity """
        cls.amenity = Amenity()
        cls.amenity.name = "spa"

    @classmethod
    def teardown_class(cls):
        """ Deletes instance and attempts to remove file if it exists """
        del cls.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """ Tests if script meets PEP8 styling """
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Fails PEP8")

    def test_functions(self):
        """ Tests for methods inside Amenity class """
        self.assertIsNotNone(Amenity.__doc__)

    def test_subclass(self):
        """ Tests if instance is a subclass of BaseModel """
        self.setup_class()
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_save(self):
        """ Tests for funcionality of save method """
        self.setup_class()
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

if __name__ == '__main__':
    unittest.main()
