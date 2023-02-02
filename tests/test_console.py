#!/usr/bin/python3
"""Test for console

all unittests for console.py, all features!

"""
import os
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test console"""

    def setUp(self):
        """Set up"""
        self.id_regex = "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}"
        "-[0-9a-f]{4}-[0-9a-f]{12}"

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
            self.assertRegex(f.getvalue().strip(), self.id_regex)

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
            self.assertRegex(f.getvalue().strip(), self.id_regex)
            HBNBCommand().onecmd("show BaseModel " + f.getvalue().strip())
            self.assertRegex(f.getvalue().strip(), self.id_regex)

    def test_destroy(self):
        """Test destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual("** class name missing **", f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy FakeClass")
            self.assertEqual("** instance id missing **", f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual("** instance id missing **", f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 1234")
            self.assertEqual("** no instance found **", f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("destroy BaseModel " + f.getvalue())
            self.assertIn("Destroyed successfully!", f.getvalue().strip())

    def test_all(self):
        """Test all"""
        # with patch('sys.stdout', new=StringIO()) as f:
        #     HBNBCommand().onecmd("all")
        #     self.assertEqual("[]", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all FakeClass")
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("all BaseModel")
            self.assertIn("BaseModel", f.getvalue().strip())

    def test_quit(self):
        """Test quit"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        """Test EOF"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


if __name__ == "__main__":
    unittest.main()
