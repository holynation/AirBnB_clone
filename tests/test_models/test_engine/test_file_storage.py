#!/usr/bin/python3
"""
Unittest for FileStorage class
"""
import unittest
import pep8
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """docstring for TestFileStorage"""

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "kindly fix pep8 issues")

    def test_check_none_for_methods(self):
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_all(self):
        """
        Tests method: all (returns the dictionary __objects)
        """
        storage = FileStorage()
        instances_all_dic = storage.all()
        self.assertIsNotNone(instances_all_dic)
        self.assertIs(instances_all_dic, storage._FileStorage__objects)
        self.assertEqual(type(instances_all_dic), dict)

    def test_new(self):
        """
        Tests method: new (sets in __objects the obj
        with key <obj class name>.id)
        """
        new_storage = FileStorage()
        instances_dic = new_storage.all()
        my_model = BaseModel()
        my_model.id = 999
        my_model.name = "my_model"
        new_storage.new(my_model)
        key = my_model.__class__.__name__ + "." + str(my_model.id)
        self.assertIsNotNone(instances_dic[key])

    def test_save(self):
        """
        Tests method: save (serializes __objects to the JSON file)
        """
        storage = FileStorage()
        storage.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_reload(self):
        """
        Tests method: reload (deserializes the
        JSON file to __objects if exists)
        """
        try:
            storage = FileStorage()
            storage.reload()
            self.assertTrue(True)
        except ValueError:
            self.assertTrue(False)
