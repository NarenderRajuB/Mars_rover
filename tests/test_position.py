import unittest
from marsrover.position import RoverPosition


class TestPosition(unittest.TestCase):

    def test_position_with_values_passed(self):
        """
        Test position instance with values passed as parameters
        """
        position = RoverPosition(3, 2)
        self.assertEqual(position.x, 3)
        self.assertEqual(position.y, 2)

    def test_position_with_default_values(self):
        """
        Test position instance with with default
        """
        position = RoverPosition()
        self.assertEqual(position.x, 0)
        self.assertEqual(position.y, 0)

    def test_position_instances_equal_operator(self):
        """
        Test position instances equality method
        """
        pos1 = RoverPosition(2, 5)
        self.assertTrue(pos1 == RoverPosition(2, 5))
        self.assertFalse(pos1 == RoverPosition(1, 2))


if __name__ == '__main__':
    unittest.main()
