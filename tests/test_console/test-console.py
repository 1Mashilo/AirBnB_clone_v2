import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO
class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        # Test create command for each class
        self.console.onecmd("create Place")
        self.assertTrue(mock_stdout.getvalue().startswith("**"))
        self.console.onecmd("create State")
        self.assertTrue(mock_stdout.getvalue().startswith("**"))
        # Add similar tests for other classes

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        # Test show command for each class
        self.console.onecmd("show Place")
        self.assertTrue(mock_stdout.getvalue().startswith("**"))
        self.console.onecmd("show State")
        self.assertTrue(mock_stdout.getvalue().startswith("**"))
        # Add similar tests for other classes

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        # Test destroy command for each class
        self.console.onecmd("destroy Place")
        self.assertTrue(mock_stdout.getvalue().startswith("**"))
        self.console.onecmd("destroy State")
        self.assertTrue(mock_stdout.getvalue().startswith("**"))
        # Add similar tests for other classes

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        # Test update command for each class
        self.console.onecmd("update Place")
        self.assertTrue(mock_stdout.getvalue().startswith("**"))
        self.console.onecmd("update State")
        self.assertTrue(mock_stdout.getvalue().startswith("**"))
        # Add similar tests for other classes

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        # Test all command for each class
        self.console.onecmd("all Place")
        self.assertTrue(mock_stdout.getvalue().startswith("["))
        self.console.onecmd("all State")
        self.assertTrue(mock_stdout.getvalue().startswith("["))
        # Add similar tests for other classes

if __name__ == '__main__':
    unittest.main()