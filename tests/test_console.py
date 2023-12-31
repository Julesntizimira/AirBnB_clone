#!/usr/bin/python3
''' define TestConsole class, unittest console app
'''
import sys
import os
from console import HBNBCommand
import unittest
from unittest.mock import patch
from io import StringIO
import uuid
from models import storage


class TestConsole(unittest.TestCase):
    ''' Test console module '''
    def setUp(self):
        '''pre-define actions automatically happens
           at the end of each test
        '''
        self.err1 = "** class name missing **"
        self.err2 = "** class doesn't exist **"
        self.err3 = "** instance id missing **"
        self.err4 = "** no instance found **"
        self.err5 = "** attribute name missing **"
        self.err6 = "** value missing **"
        self.err = "*** Unknown syntax: "

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.str1 = output.getvalue().strip()
            print("hello world")

    def tearDown(self):
        '''pre-define actions automatically happens
           at the end of each test
        '''
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(f"destroy User {self.str1}"))

    def test_quit_exits(self):
        '''test do_quit method'''
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        '''test do_EOF method'''
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_help(self):
        str1 = ("Documented commands (type help <topic>):\n"
                "========================================\n"
                "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(str1.strip(), output.getvalue().strip())

    def test_help_create(self):
        '''test help create command'''
        str1 = HBNBCommand.do_create.__doc__
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(str1.strip(), output.getvalue().strip())

    def test_help_all(self):
        '''test help all command'''
        str1 = HBNBCommand.do_all.__doc__
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(str1.strip(), output.getvalue().strip())

    def test_help_show(self):
        '''test help show command'''
        str1 = HBNBCommand.do_show.__doc__
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(str1.strip(), output.getvalue().strip())

    def test_help_count(self):
        '''test help count command'''
        str1 = HBNBCommand.do_count.__doc__
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(str1.strip(), output.getvalue().strip())

    def test_help_update(self):
        '''test help update command'''
        str1 = HBNBCommand.do_update.__doc__
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(str1.strip(), output.getvalue().strip())

    def test_help_EOF(self):
        '''test help EOF command'''
        str1 = HBNBCommand.do_EOF.__doc__
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(str1.strip(), output.getvalue().strip())

    def test_help_quit(self):
        '''test help quit command'''
        str1 = HBNBCommand.do_quit.__doc__
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(str1.strip(), output.getvalue().strip())

    def test_create(self):
        '''test create command with an existing class'''
        length = len(str(uuid.uuid4()))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertEqual(length, len(output.getvalue().strip()))

        """ test with name of class missing """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(self.err1, output.getvalue().strip())

        """test create with not existing class"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create jhghg"))
            self.assertEqual(self.err2, output.getvalue().strip())

    def test_show(self):
        '''test show with class missing'''
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(self.err1, output.getvalue().strip())

        """test show with non-existing class"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show jhghg"))
            self.assertEqual(self.err2, output.getvalue().strip())

        """test create with missing instance id"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show User"))
            self.assertEqual(self.err3, output.getvalue().strip())

        """test with non-existing instance id"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show User 87668232"))
            self.assertEqual(self.err4, output.getvalue().strip())

        """test with existing instance id"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(f"show User {self.str1}"))
            self.assertIn(self.str1, output.getvalue().strip())

    def test_destroy(self):
        '''test  with class missing'''
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(self.err1, output.getvalue().strip())

        """test with non-existing class"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy jhghg"))
            self.assertEqual(self.err2, output.getvalue().strip())

        """test with missing instance id"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertEqual(self.err3, output.getvalue().strip())

        """test non-existing instance id"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy User 87668232"))
            self.assertEqual(self.err4, output.getvalue().strip())

        """test with existing instance id"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(f"destroy User {self.str1}"))
            self.assertEqual("", output.getvalue().strip())

    def test_all(self):
        """test with non-existing class"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all jhghg"))
            self.assertEqual(self.err2, output.getvalue().strip())

        """test with existing class"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
            self.assertIn(self.str1, output.getvalue().strip())

        """test with missing class"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertIn(self.str1, output.getvalue().strip())

    def test_count(self):
        """test count"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("count User"))
            self.assertTrue(eval(output.getvalue().strip()) >= 1)

        '''test  with class missing'''
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("count"))
            self.assertEqual(self.err1, output.getvalue().strip())

        """test with non-existing class"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("count jhghg"))
            self.assertEqual(self.err2, output.getvalue().strip())

    def test_update(self):
        '''test  with class missing'''
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(self.err1, output.getvalue().strip())

        """test with non-existing class"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update jhghg"))
            self.assertEqual(self.err2, output.getvalue().strip())

        """test with missing instance id"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update User"))
            self.assertEqual(self.err3, output.getvalue().strip())

        """test non-existing instance id"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update User 87668232"))
            self.assertEqual(self.err4, output.getvalue().strip())

        """test with attribute name missing"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(f"update User {self.str1}"))
            self.assertEqual(self.err5, output.getvalue().strip())

        """test with value missing"""
        line1 = f"update User {self.str1} first_name"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(line1))
            self.assertEqual(self.err6, output.getvalue().strip())

        """test with more than one attr-value"""
        line2 = f"update User {self.str1} first_name 'john' Age 32"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(line2))
            self.assertFalse(HBNBCommand().onecmd(f"show User {self.str1}"))
            self.assertNotIn('Age: 32', output.getvalue().strip())

        """test created_at and updated_at attribute"""
        obj = storage.all()
        obj_key = f"User.{self.str1}"
        obj_value = obj[obj_key]
        self.assertNotEqual(obj_value.created_at, obj_value.updated_at)

    def test_prompt_string(self):
        '''test prompt string'''
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        '''test HBNBCommand command with empty line'''
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
