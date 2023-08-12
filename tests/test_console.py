import unittest
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.hbnb_cmd = HBNBCommand()

    @patch("builtins.input", side_effect=["quit"])
    def test_quit_command(self, mock_input):
        self.assertTrue(self.hbnb_cmd.onecmd("quit"))

    @patch("builtins.input", side_effect=["EOF"])
    def test_eof_command(self, mock_input):
        self.assertTrue(self.hbnb_cmd.onecmd("EOF"))


if __name__ == "__main__":
    unittest.main()
