# Testing the AirBnB clone console
import unittest
from unittest.mock import patch
from io import StringIO
import os
import pycodestyle
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

class ConsoleTest(unittest.TestCase):
    """This class will run tests on the console"""

    @classmethod
    def setUpClass(cls):
        """Setting up for the test"""
        cls.shell = HBNBCommand()

    @classmethod
    def tearDown(cls):
        """Tearing down at the end of the test"""
        del cls.shell

    def tearDown(self):
        """Removing temporary file (file.json) created"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_console(self):
        """Check for PEP8 compliance."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, 'Fix PEP8')

    def test_docstrings_in_console(self):
        """Check for docstrings."""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_show(self):
        """Test the show command input."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.shell.onecmd("show")
            self.assertEqual(
                "** missing class name **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.shell.onecmd("show classnonexistent")
            self.assertEqual(
                "** class does not exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.shell.onecmd("show BaseModel")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.shell.onecmd("show BaseModel id01")
            self.assertEqual(
                "** instance not found **\n", f.getvalue())
