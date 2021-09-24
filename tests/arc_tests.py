import unittest
from gcodeBuddy import Arc


class CommandTestCase(unittest.TestCase):

    def setUp(self):
        """Creating Arc object to test"""
        self.command = Arc(center=[0, 0], radius=1.0, start_angle=0, end_angle=180, direction="cc")

    def test_get_center(self):
        """Test get_center() method"""
        # should return [0, 0]
        result = self.command.get_center()
        self.assertEqual(result, [0, 0], msg="test_get_center()")

    def test_get_radius(self):
        """Test get_radius() method"""
        # should return 1.0
        result = self.command.get_radius()
        self.assertEqual(result, 1.0, msg="test_get_radius()")

    def test_get_start_angle(self):
        """Test get_start_angle() method"""
        # should return 0
        result = self.command.get_start_angle()
        self.assertEqual(result, 0, msg="test_get_start_angle()")

    def test_get_end_angle(self):
        """Test get_end_angle() method"""
        # should return 360
        result = self.command.get_end_angle()
        self.assertEqual(result, 180, msg="test_get_end_angle()")

    def test_get_direction(self):
        """Test get_direction() method"""
        # should return "cc"
        result = self.command.get_direction()
        self.assertEqual(result, "cc", msg="test_get_direction()")

    def test_get_angle(self):
        """Test get_angle() method"""
        # should return 180
        result = self.command.get_angle()
        self.assertEqual(result, 180, msg="test_get_angle()")

    def test_set_center(self):
        """Test set_center() method"""
        self.command.set_center([-1, -1])
        # should return [-1, -1]
        result = self.command.get_center()
        self.assertEqual(result, [-1, -1], msg="test_set_center()")

    def test_set_radius(self):
        """Test set_radius() method"""
        self.command.set_radius(1)
        # should return 1
        result = self.command.get_radius()
        self.assertEqual(result, 1, msg="test_set_radius()")

    def test_set_start_angle(self):
        """Test set_start_angle() method"""
        self.command.set_start_angle(30)
        # should return 30
        result = self.command.get_start_angle()
        self.assertEqual(result, 30, msg="test_set_start_angle()")

    def test_set_end_angle(self):
        """Test set_end_angle() method"""
        self.command.set_end_angle(150)
        # should return 330
        result = self.command.get_end_angle()
        self.assertEqual(result, 150, msg="test_set_end_angle()")

    def test_set_direction(self):
        """Test set_direction() method"""
        self.command.set_direction("c")
        # should return "c"
        result = self.command.get_direction()
        self.assertEqual(result, "c", msg="test_set_direction()")
