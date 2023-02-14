#!/usr/bin/python3
""" Tests class State """
import unittest
from models.state import State
from models.base_model import BaseModel
import os
import pep8


class TestState(unittest.TestCase):
    """ Tests different attributes and functionality of State class """

    @classmethod
    def setup_class(cls):
        """ Sets up an instance of State """
        cls.state = State()
        cls.state.name = "Oregon"

    @classmethod
    def teardown_class(cls):
        """ Deletes instance and attempts to remove file if it exists """
        del cls.state
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """ Tests if script meets PEP8 styling """
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Fails PEP8")

    def test_functions(self):
        """ Tests for methods inside State class """
        self.assertIsNotNone(State.__doc__)

    def test_subclass(self):
        """ Tests if instance is a subclass of BaseModel """
        self.setup_class()
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_save(self):
        """ Tests for funcionality of save method """
        self.setup_class()
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

if __name__ == '__main__':
    unittest.main()
