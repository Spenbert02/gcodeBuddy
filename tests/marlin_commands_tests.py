import unittest
from gcodeBuddy.marlin import marlin_commands


class MarlinCommandsTestCase(unittest.TestCase):

    def setUp(self):
        """Calling and storing return value of marlin_commands() function"""
        self.command_tuple = marlin_commands()

    def test_return__type(self):
        """Test returns object of type tuple"""
        self.assertEqual(type(self.command_tuple), tuple, msg="test_return_type()")

    def test_element_types(self):
        """Test every entry in tuple is type string"""
        all_string = True
        for command in self.command_tuple:
            if not isinstance(command, str):
                all_string = False
        self.assertEqual(all_string, True, msg="test_element_types")

    def test_first_letter(self):
        """Ensuring every command begins with legal letters"""
        valid = True
        for command in self.command_tuple:
            if command[0] not in ("G", "M", "T"):
                valid = False
        self.assertEqual(valid, True, msg="test_first_letter()")