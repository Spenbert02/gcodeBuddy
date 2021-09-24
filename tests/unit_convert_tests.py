import unittest
from gcodeBuddy import unit_convert


class UnitConvertTestCase(unittest.TestCase):

    def test_category_alignment(self):
        """Test result of impossible conversion"""
        # should return None
        result = unit_convert(1, "mm", "in/min")
        self.assertEqual(result, None, msg="test_category_alignment()")

    def test_distance_conversion(self):
        """Test simple distance conversion"""
        # should return 10 (10.0, rounded down to 10)
        result = int(unit_convert(1, "cm", "mm"))
        self.assertEqual(result, 10, msg="test_distance_conversion()")

    def test_speed_conversion(self):
        """Test simple speed conversion"""
        # should return 10
        result = int(unit_convert(1, "cm/sec", "mm/sec"))
        self.assertEqual(result, 10, msg="test_speed_conversion()")
