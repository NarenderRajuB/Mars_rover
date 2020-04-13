import unittest
from marsrover.plateau import Plateau
from marsrover.position import RoverPosition


class TestPlateau(unittest.TestCase):
    def test_plateau_instance(self):
        """
        Test Plateau instance grid dimensions
        """
        plateau = Plateau(5, 7)
        self.assertEqual(plateau.width, 5)
        self.assertEqual(plateau.height, 7)

    def test_move_available(self):
        """
        Test to check of the Move is possible for the Rover in the Plateau
        """
        plateau = Plateau(5, 7)
        self.assertTrue(plateau.is_position_within_plateau_area(RoverPosition(2, 3)))
        self.assertFalse(plateau.is_position_within_plateau_area(RoverPosition(6, 2)))
        self.assertFalse(plateau.is_position_within_plateau_area(RoverPosition(3, 8)))
        self.assertFalse(plateau.is_position_within_plateau_area(RoverPosition(-1, 2)))
        self.assertFalse(plateau.is_position_within_plateau_area(RoverPosition(-1, -1)))


if __name__ == '__main__':
    unittest.main()

