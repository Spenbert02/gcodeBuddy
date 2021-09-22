import unittest
from gcodeBuddy.marlin import Command


class CommandTestCase(unittest.TestCase):

    def setUp(self):
        """Creating Command object to test"""
        self.line = Command("G0 X1 Y-2 Z49 E4")

    def test_get_command(self):
        """Test proper command is interpreted"""
        # should return G0
        result = self.line.get_command()
        self.assertEqual(result, "G0", msg="test_get_command()")

    def test_has_param_false(self):
        """Test no extraneous parameters are interpreted"""
        # should return False
        result = self.line.has_param("S")
        self.assertEqual(result, False, msg="test_has_param_false()")

    def test_has_param_true(self):
        """Test existing parameters are properly interpreted"""
        # should return True
        result = self.line.has_param("X")
        self.assertEqual(result, True, msg="test_has_param_true()")

    def test_get_param_positive(self):
        """Test proper positive parameter values are interpreted"""
        # should return 49.7
        result = self.line.get_param("E")
        self.assertEqual(result, 4, msg="test_get_param_positive()")

    def test_get_param_negative(self):
        """Test proper negative parameter values are interpreted"""
        # should return -1.90
        result = self.line.get_param("Y")
        self.assertEqual(result, -2, msg="test_get_param_negative()")

    def test_set_param(self):
        """Test proper parameter values are set"""
        # should return 49
        self.line.set_param("Z", 49)
        result = self.line.get_param("Z")
        self.assertEqual(result, 49, msg="test_set_param()")

    def test_get_string(self):
        """Test proper string is returned"""
        result = self.line.get_string()
        self.assertEqual(result, "G0 X1.0 Y-2.0 Z49.0 E4.0", msg="test_get_string()")

if __name__ == "__main__":
    unittest.main()