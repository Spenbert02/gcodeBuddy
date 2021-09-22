import unittest
from gcodeBuddy import angle

class AngleTestCase(unittest.TestCase):

    def test_non_origin_center(self):
        """Test angle with center point not on origin"""
        # should return 45
        test_angle = angle((1, 1), (2, 2))
        # should return True
        result = abs(test_angle - 45) < 0.001  # approximate equality - I hate floats
        self.assertEqual(result, True, msg="test_non_origin_center()")

    def test_pos_x_axis(self):
        """Test angle of point on positive x-axis"""
        # should return 0
        result = angle((0, 0), (1, 0))
        self.assertEqual(result, 0, msg="test_pos_x_axis()")

    def test_small_quad_I(self):
        """Test angle of point near positive x axis in quadrant I"""
        # should return ~5.710593137
        test_angle = angle((0, 0), (10, 1))
        # should return True
        result = abs(test_angle - 5.710593137) < 0.001
        self.assertEqual(result, True, msg="test_small_quad_I()")

    def test_pos_y_axis(self):
        """Test angle of point on positive y axis"""
        # should return 90
        result = angle((0, 0), (0, 1))
        self.assertEqual(result, 90, msg="test_pos_y_axis()")

    def test_small_quad_II(self):
        """Test angle of point near positive y axis in quadrant II"""\
        # should return ~95.71058314
        test_angle = angle((0, 0), (-1, 10))
        # should return True
        result = abs(test_angle - 95.71058314) < 0.001
        self.assertEqual(result, True, msg="test_small_quad_II()")

    def test_neg_x_axis(self):
        """Test angle of point on negative x axis"""
        # should return 180
        result = angle((0, 0), (-1, 0))
        self.assertEqual(result, 180, msg="test_neg_x_axis()")

    def test_small_quad_III(self):
        """Test angle of point near negative x axis in quadrant III"""
        # should return ~185.71105931
        test_angle = angle((0, 0), (-10, -1))
        # should return True
        result = abs(test_angle - 185.71105931) < 0.001
        self.assertEqual(result, True, msg="test_small_quad_III()")

    def test_neg_y_axis(self):
        """Test angle of point on negative y axis"""
        # should return 270
        result = angle((0, 0), (0, -1))
        self.assertEqual(result, 270, msg="test_neg_y_axis()")

    def test_small_quad_IV(self):
        """Test angle of point near negative y axis in quadrant IV"""
        # should return ~275.7105931
        test_angle = angle((0, 0), (1, -10))
        # should return True
        result = abs(test_angle - 275.7105931) < 0.001
        self.assertEqual(result, True, msg="test_small_quad_IV()")
