import unittest
from unittest.mock import patch, MagicMock
from console import HBNBCommand  # Replace with the actual module name


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.hbnb_cmd = HBNBCommand()

    @patch("builtins.input", side_effect=["quit"])
    def test_quit_command(self, mock_input):
        self.assertTrue(self.hbnb_cmd.onecmd("quit"))

    @patch("builtins.input", side_effect=["EOF"])
    def test_eof_command(self, mock_input):
        self.assertTrue(self.hbnb_cmd.onecmd("EOF"))

    @patch("builtins.print")
    @patch("models.storage.all", return_value={'BaseModel.123': "mock_instance"})
    def test_validate_class_and_id_valid(self, mock_all, mock_print):
        class_name, key = self.hbnb_cmd.validate_class_and_id("BaseModel 123")
        self.assertEqual(class_name, "BaseModel")
        self.assertEqual(key, "BaseModel.123")
        mock_print.assert_not_called()

    @patch("builtins.print")
    @patch("models.storage.all", return_value={})
    def test_validate_class_and_id_missing_instance(self, mock_all, mock_print):
        class_name, key = self.hbnb_cmd.validate_class_and_id("BaseModel 123")
        self.assertIsNone(class_name)
        self.assertIsNone(key)
        mock_print.assert_called_once_with("** no instance found **")

    # Add more test cases for validate_class_and_id

    @patch("builtins.print")
    @patch("models.storage.all")
    def test_do_create_valid(self, mock_all, mock_print):
        mock_all.return_value = {}
        with patch.dict(self.hbnb_cmd.classes, {'BaseModel': MagicMock()}):
            self.hbnb_cmd.do_create("BaseModel")
            mock_print.assert_called_once()

    @patch("builtins.print")
    @patch("models.storage.all")
    def test_do_create_missing_class(self, mock_all, mock_print):
        mock_all.return_value = {}
        self.hbnb_cmd.do_create("NonExistentClass")
        mock_print.assert_called_once_with("** class doesn't exist **")


    @patch("builtins.print")
    @patch("models.storage.all")
    @patch("console.HBNBCommand.validate_class_and_id", return_value=("BaseModel", "BaseModel.123"))
    def test_do_show_valid(self, mock_validate, mock_all, mock_print):
        mock_all.return_value = {'BaseModel.123': MagicMock()}
        self.hbnb_cmd.do_show("BaseModel 123")
        mock_print.assert_called_once()


    @patch("builtins.print")
    @patch("models.storage.all")
    def test_do_show_missing_class(self, mock_all, mock_print):
        mock_all.return_value = {}
        self.hbnb_cmd.do_show("NonExistentClass 123")
        mock_print.assert_called_once_with("** class doesn't exist **")


    @patch("builtins.print")
    @patch("models.storage.all")
    @patch("console.HBNBCommand.validate_class_and_id", return_value=("BaseModel", "BaseModel.123"))
    def test_do_destroy_valid(self, mock_validate, mock_all, mock_print):
        mock_all.return_value = {'BaseModel.123': MagicMock()}
        self.hbnb_cmd.do_destroy("BaseModel 123")
        mock_print.assert_not_called()

    @patch("builtins.print")
    @patch("models.storage.all")
    def test_do_destroy_missing_class(self, mock_all, mock_print):
        mock_all.return_value = {}
        self.hbnb_cmd.do_destroy("NonExistentClass 123")
        mock_print.assert_called_once_with("** class doesn't exist **")



    @patch("builtins.print")
    @patch("models.storage.all")
    @patch("console.HBNBCommand.validate_class_and_id", return_value=("BaseModel", "BaseModel.123"))
    def test_do_update_valid(self, mock_validate, mock_all, mock_print):
        mock_all.return_value = {'BaseModel.123': MagicMock()}
        self.hbnb_cmd.do_update("BaseModel 123 name 'new_name'")
        mock_print.assert_not_called()


    @patch("builtins.print")
    @patch("models.storage.all")
    def test_do_update_missing_class(self, mock_all, mock_print):
        mock_all.return_value = {}
        self.hbnb_cmd.do_update("NonExistentClass 123 name 'new_name'")
        mock_print.assert_called_once_with("** class doesn't exist **")

    @patch("builtins.print")
    @patch("models.storage.all")
    def test_do_all_existing_class(self, mock_all, mock_print):
        mock_all.return_value = {'BaseModel.123': MagicMock()}
        self.hbnb_cmd.do_all("BaseModel")
        mock_print.assert_called_once()

    @patch("builtins.print")
    @patch("models.storage.all")
    def test_do_all_nonexistent_class(self, mock_all, mock_print):
        mock_all.return_value = {}
        self.hbnb_cmd.do_all("NonExistentClass")
        mock_print.assert_called_once_with("** class doesn't exist **")
