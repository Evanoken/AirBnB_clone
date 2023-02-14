#!/usr/bin/python3
""" Tests class Amenity """
import unittest
from models.user import User
from models.base_model import BaseModel
import os
import pep8


class TestUser(unittest.TestCase):
    """ Tests different attributes and functionality of User class """

    @classmethod
    def setup_class(cls):
        """ Sets up an instance of User """
        cls.user = User()
        cls.user.first_name = "Betty"
        cls.user.last_name = "Holberton"
        cls.user.email = "hello@holbertonschool.com"
        cls.user.password = "password123"

    @classmethod
    def teardown_class(cls):
        """ Deletes instance and attempts to remove file if it exists """
        del cls.user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """ Tests if script meets PEP8 styling """
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "Fails PEP8")

    def test_functions(self):
        """ Tests for methods inside User class """
        self.assertIsNotNone(User.__doc__)

    def test_subclass(self):
        """ Tests if instance is a subclass of BaseModel """
        self.setup_class()
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_save(self):
        """ Tests for funcionality of save method """
        self.setup_class()
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

if __name__ == '__main__':
    unittest.main()
