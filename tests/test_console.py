#!/usr/bin/python3
"""Test for console

all unittests for console.py, all features!

"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """Test console"""

    def test_create(self):
        """Test create"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **", f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create FakeClass")
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id_regex = "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}"
            "-[0-9a-f]{4}-[0-9a-f]{12}"
            self.assertRegex(f.getvalue().strip(), id_regex)

    def test_show(self):
        """Test show"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual("** class name missing **", f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show FakeClass")
            self.assertEqual("** instance id missing **", f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual("** instance id missing **", f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 1234")
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id_regex = "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}"
            "-[0-9a-f]{4}-[0-9a-f]{12}"
            self.assertRegex(f.getvalue().strip(), id_regex)
            HBNBCommand().onecmd("show BaseModel " + f.getvalue().strip())
            self.assertRegex(f.getvalue().strip(), id_regex)

if __name__ == "__main__":
    unittest.main()
