import unittest
import numpy as np
from gcodeBuddy import centers_from_params as center


class CentersFromParamsTestCase(unittest.TestCase):

    def test_horizontal_points(self):
        """Test centers of horizontal points"""
        # should return (4, 3), (4, -3)
        center_1, center_2 = center((0, 0), (8, 0), 5)
        # should return True
        result = [center_1, center_2] == [[4, 3], [4, -3]]
        self.assertEqual(result, True, msg="test_horizontal_points()")

    def test_vertical_points(self):
        """Test centers of vertical points"""
        # should return (3, 4), (-3, 4)
        center_1, center_2 = center((0, 0), (0, 8), 5)
        # should return True
        result = [center_1, center_2] == [[3, 4],[-3, 4]]
        self.assertEqual(result, True, msg="test_vertical_points()")

    def test_quad_I(self):
        """Tests centers with one point on origin, one point in quad I"""
        # should return (0, 4), (4, 0)
        center_1, center_2 = center((0, 0), (4, 4), 4)
        # should return True
        result = [center_1, center_2] == [[4, 0], [0, 4]]
        self.assertEqual(result, True, msg="test_quad_I()")

    def test_quad_II(self):
        """Tests centers with one point on the origin and one point in quad II"""
        # should return (0, 4), (-4, 0)
        center_1, center_2 = center((0, 0), (-4, 4), 4)
        # should return True
        result = [center_1, center_2] == [[0, 4], [-4, 0]]
        self.assertEqual(result, True, msg="test_quad_II()")

    def test_quad_III(self):
        """Tests centers with one point on the origin and one point in quad III"""
        # should return (-4,0), (0, -4)
        center_1, center_2 = center((0, 0), (-4, -4), 4)
        # should return True
        result = [center_1, center_2] == [[-4, 0], [0, -4]]
        self.assertEqual(result, True, msg="test_quad_III()")

    def test_quad_IV(self):
        """Tests centers with one point on the origin and one point in quad IV"""
        # should return (4, 0), (-4, 0)
        center_1, center_2 = center((0, 0), (4, -4), 4)
        # should return True
        result = [center_1, center_2] == [[4, 0], [0, -4]]
        self.assertEqual(result, True, msg="test_quad_IV()")
