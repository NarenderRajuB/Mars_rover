import unittest
from marsrover.rover import Rover
from marsrover.plateau import Plateau, InvalidCoordinateError, InvalidDirectionError
from marsrover.position import Position


class TestRover(unittest.TestCase):
    def setUp(self):
        self.plateau_dimensions = Plateau(8, 4)
        self.rover_initial_position = Position(2, 1)

    def test_rover_instance(self):
        """
        Test rover instance
        """
        plateau_grid = Plateau(7, 7)
        position = Position(0, 0)

        rover = Rover(plateau_grid, position, Rover.DIRECTIONS['W'])
        self.assertEqual(position, rover._position)
        self.assertEqual(plateau_grid, rover._plateau)

        rover.set_position(3, 3, Rover.DIRECTIONS.get('E'))
        self.assertEqual(rover._position.x, 3)
        self.assertEqual(rover._position.y, 3)
        self.assertEqual(rover.get_heading, 'E')

    def test_rover_position(self):
        """
        Test rover position after performing movements
        """
        rover = Rover(self.plateau_dimensions, self.rover_initial_position, Rover.DIRECTIONS.get('E'))
        rover.execute_instructions("LMLM")
        self.assertEqual(rover._position.x, 1)
        self.assertEqual(rover._position.y, 2)
        self.assertEqual(rover.get_heading, 'W')

    def test_get_heading(self):
        """
        Test the rover heading direction
        """
        rover = Rover(self.plateau_dimensions, self.rover_initial_position, Rover.DIRECTIONS.get('E'))
        self.assertEqual(rover.get_heading, 'E')

    def test_get_heading_raise_exception(self):
        """
        Test for exception for invalid rover heading direction from the the instructions
        """
        rover = Rover(self.plateau_dimensions, self.rover_initial_position, 8)
        with self.assertRaises(InvalidDirectionError):
            rover.get_heading

    def test_execute_instructions_raise_invalid_coordinate_exception(self):
        """
        Test for Invalid Coordinate exception if rover is moved out of Plateau grid dimensions
        """
        with self.assertRaises(InvalidCoordinateError):
            rover = Rover(self.plateau_dimensions, self.rover_initial_position, Rover.DIRECTIONS.get('E'))
            rover.execute_instructions('RMMM')


if __name__ == '__main__':
    unittest.main()
