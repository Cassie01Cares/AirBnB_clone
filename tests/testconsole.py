from unittest.mock import patch
from io import StringIO
import unittest
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.cmd = HBNBCommand()

    def tearDown(self):
        self.cmd = None

    def test_help(self):
        """Test the functionality of the help command"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        output = """
Documented commands (type help <topic>):
========================================
EOF  help  quit


        """

        self.assertEqual(output.strip(), f.getvalue().strip())

    def test_help_EOF(self):
        """test the functionality of the help-EOF command
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
        output = """Handles End Of File character\n
        """
        self.assertEqual(output.strip(), f.getvalue().strip())


    def test_help_quit(self):
        """to test the functionality of help quit command"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        output = """Quit command to exit the program \n
        """
        self.assertEqual(output.strip(), f.getvalue().strip())

    def test_emptyline(self):
        """to test the functionality of emptyline
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("emptyline")
        output = """*** Unknown syntax: emptyline"""
        self.assertEqual(output.strip(), f.getvalue().strip())

if __name__ == '__main__':
    unittest.main()

