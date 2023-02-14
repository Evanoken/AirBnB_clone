#!/usr/bin/python3
""" Tests class Review """
import unittest
from models.review import Review
from models.base_model import BaseModel
import os
import pep8


class TestReview(unittest.TestCase):
    """ Tests different attributes and functionality of Review class """

    @classmethod
    def setup_class(cls):
        """ Sets up an instance of Review """
        cls.review = Review()
        cls.review.place_id = "Holberton School"
        cls.review.user_id = "Julian"
        cls.review.text = "100%"

    @classmethod
    def teardown_class(cls):
        """ Deletes instance and attempts to remove file if it exists """
        del cls.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """ Tests if script meets PEP8 styling """
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "Fails PEP8")

    def test_functions(self):
        """ Tests for methods inside Review class """
        self.assertIsNotNone(Review.__doc__)

    def test_subclass(self):
        """ Tests if instance is a subclass of BaseModel """
        self.setup_class()
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    def test_save(self):
        """ Tests for funcionality of save method """
        self.setup_class()
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

if __name__ == '__main__':
    unittest.main()
