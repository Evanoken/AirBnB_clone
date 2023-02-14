#!/usr/bin/python3
from models.base_model import BaseModel
import pep8
import unittest
"""
Unittesting for base_model
"""


class TestBaseModel(unittest.TestCase):
    """
    instance id's should not be equal to one another

    """
    @classmethod
    def setup_class(cls):
        """ Sets up an instance of BaseModel """
        cls.bm = BaseModel()
        cls.bm.name = "Betty"
        cls.bm.my_number = 100

    @classmethod
    def teardown_class(cls):
        """ Deletes instance of BaseModel """
        del cls.bm1

    def test_pep8(self):
        """ Tests script for PEP8 styling """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, 'Fails PEP8')

    def test_docstrings(self):
        """ Tests whether methods in BaseModel has docstrings """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_id(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)
        self.assertIsInstance(bm2, BaseModel)
        self.assertTrue(hasattr(bm2, "id"))
        self.assertIsInstance(bm2.id, str)

    def test_created_updated(self):
        self.setup_class()
        self.assertTrue(isinstance(self.bm, BaseModel))
        self.assertEqual(self.bm.created_at, self.bm.updated_at)

if __name__ == '__main__':
    unittest.main()
