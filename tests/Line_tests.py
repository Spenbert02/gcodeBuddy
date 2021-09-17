import unittest
from gcodeBuddy import Line

class Line_test_case(unittest.TestCase):

    def setUp(self):
        self.line = Line("G0 X1.2 Y-2 Z49.7 E4")

    def test_get_command(self):
        """Test proper command is interpreted"""
        # should return G0
        result = self.line.get_command()
        self.assertEqual(result, "G0")

    def test_has_param_false(self):
        """Test no extraneous parameters are interpreted"""
        # should return False
        result = self.line.has_param("S")
        self.assertEqual(result, False)

    def test_has_param_true(self):
        """Test existing parameters are properly interpreted"""
        # should return True
        result = self.line.has_param("X")
        self.assertEqual(result, True)

    def test_get_param_positive(self):
        """Test proper positive parameter values are interpreted"""
        # should return 49.7
        result = self.line.get_param("E")
        self.assertEqual(result, 4)

    def test_get_param_negative(self):
        """Test proper negative parameter values are interpreted"""
        # should return -1.90
        result = self.line.get_param("Y")
        self.assertEqual(result, -2)

if __name__ == "__main__":
    unittest.main()