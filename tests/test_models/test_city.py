#!/usr/bin/python3
""" Tests class City class """
import models
from models.city import City
from models.base_model import BaseModel
import os
import pep8
import unittest


class TestCity(unittest.TestCase):
    """ Tests different attributes and functionality of City class """

    @classmethod
    def setup_class(cls):
        """ Creates an instance of Class and its attributes """
        cls.city = City()
        cls.city.name = "Oakland"
        cls.city.state_id = "California"

    @classmethod
    def teardown_class(cls):
        """ Deletes the instance of City class and its JSON file """
        del cls.city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_functions(self):
        """ Checks for methods """
        self.assertIsNotNone(City.__doc__)

    def test_pep8(self):
        """ Tests if script meets PEP8 styling """
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Fails PEP8")

    def test_subclass(self):
        """ Tests if the instance is a subclass of BaseModel """
        self.setup_class()
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_save(self):
        """ Tests for funcionality of save method """
        self.setup_class()
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

if __name__ == '__main__':
    unittest.main()
