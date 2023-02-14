#!/usr/bin/python3
""" Tests console """
import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """ Tests console """

    @classmethod
    def setUpClass(cls):
        """ Creates an instance """
        cls.console = HBNBCommand()

    @classmethod
    def teardown(cls):
        """ Deletes the instance """
        del cls.console

    def tearDown(self):
        """ Removes the JSON file """
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8_console(self):
        """ Tests this script for PEP8 styling """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, 'PEP8 Failed')

    def test_docstrings(self):
        """ Checks methods for docstrings """
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_empty(self):
        """ Tests the emptyline method """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_quit(self):
        """ Tests the quit method """
        with patch('sys.stdout', new=StringIO()) as f:
            with self.assertRaises(SystemExit):
                self.console.onecmd("quit")
            self.assertEqual('', f.getvalue())
