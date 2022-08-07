#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
import pep8
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_temp = BaseModel()
        cls.base_temp.name = "Anabel"
        cls.base_temp.my_weight = 60

    @classmethod
    def tearDownClass(cls):
        del cls.base_temp
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_styles_check(self):
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "kindly fix pep8 issues")

    def test_check_none_for_methods(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_instance_methods_attributes(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        self.assertTrue(isinstance(self.base_temp, BaseModel))

    def test_save(self):
        self.base_temp.save()
        self.assertNotEqual(self.base_temp.created_at,
                            self.base_temp.updated_at)

    def test_to_dict(self):
        base_temp_dict = self.base_temp.to_dict()  # convert to dict
        self.assertEqual(self.base_temp.__class__.__name__, 'BaseModel')
        self.assertIsNotNone(base_temp_dict['id'])
        self.assertIsNotNone(base_temp_dict['created_at'])
        self.assertIsNotNone(base_temp_dict['updated_at'])
        self.assertIsInstance(base_temp_dict['id'], str)
        self.assertIsInstance(base_temp_dict['created_at'], str)
        self.assertIsInstance(base_temp_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
