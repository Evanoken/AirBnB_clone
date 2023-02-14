#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
import os
import pep8
import unittest
"""
Unittesting for file_storage
"""


class TestFileStorage(unittest.TestCase):
    """
    Testing methods within FileStorage class
    """
    @classmethod
    def setup_class(cls):
        """ Creates instance of a class to test """
        cls.user = User()
        cls.user.first_name = "Betty"
        cls.user.last_name = "Holberton"
        cls.user.email = "betty@holbertonschool.com"
        cls.user.password = "password123"

    @classmethod
    def teardown_class(cls):
        """ Deletes instance of the class """
        del cls.user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """ Tests this script for PEP8 styling """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "Fails PEP8")

    def test_all(self):
        """ Tests all() method """
        fs1 = FileStorage()
        instance_dict = fs1.all()
        self.assertIsNotNone(instance_dict)
        self.assertEqual(type(instance_dict), dict)
        self.assertIs(instance_dict, fs1._FileStorage__objects)

    def test_new(self):
        """ Tests new() method """
        self.setup_class()
        fs = FileStorage()
        fs.new(self.user)
        self.assertIsNotNone(fs.all())

    def test_save(self):
        """ Tests save() method """
        bm1 = BaseModel()
        fs1 = FileStorage()
        fs1.new(bm1)
        fs1.save()
        self.assertEqual(os.path.exists('file.json'), True)

    def test_reload(self):
        """ Tests reload() method """
        bm1 = BaseModel()
        fs1 = FileStorage()
        fs1.new(bm1)
        fs1.save()
        dict1 = fs1.reload()
        # check reload() output
        self.assertTrue(dict1 is fs1.reload())

if __name__ == '__main__':
    unittest.main()
