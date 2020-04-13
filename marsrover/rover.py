from .position import RoverPosition
from .plateau import InvalidDirectionError, InvalidCoordinateError


class Rover(object):
    # TODO: active available commands and execute key values
    AVAILABLE_COMMANDS = {
        'M': 'move',
        'L': 'turn_left',
        'R': 'turn_right',
    }

    DIRECTIONS = {
        'N': 1,
        'E': 2,
        'S': 3,
        'W': 4,
    }

    heading = DIRECTIONS['N']

    def __init__(self, plateau, position, heading):
        """
        Initializing mars rover with below params
        :param plateau:
        :param position: x,y coordinates of rove
        :param heading: Direction in which rover is heading
        """
        self._plateau = plateau
        self._position = position
        self._heading = heading

        if isinstance(position, RoverPosition) and not plateau.is_position_within_plateau_area(self._position):
            print('exception')
            raise InvalidCoordinateError('rover asdasd initial position out of plateau area')

    def __str__(self):
        return self.current_position

    def set_position(self, x, y, heading):
        if not isinstance(self._position, RoverPosition):
            self._position = RoverPosition(x, y)
        else:
            self._position.x = x
            self._position.y = y
        if not self._plateau.is_position_within_plateau_area(self._position):
            raise InvalidCoordinateError('rover initial position out of plateau area')
        self._heading = heading

    @property
    def current_position(self):
        """
        Get the current position of the rover
        """
        return '{0} {1} {2}'.format(self._position.x, self._position.y, self.get_heading)

    @property
    def get_heading(self):
        """
        Get the rover heading direction
        """
        directions = list(self.DIRECTIONS.keys())

        try:
            direction = directions[self._heading - 1]
        except IndexError:
            direction = 'N'
            raise InvalidDirectionError('Invalid Directions default to North')

        return direction

    def execute_instructions(self, rover_commands):
        """
        perform the rover moves from the commands given.
        raise InvalidDirectionError if the invalid directions is instructed
        :param rover_commands: rover movement instructions

        """
        try:
            for command in rover_commands:
                if command is 'L':
                    self.turn_left()
                elif command is 'R':
                    self.turn_right()
                elif command is 'M':
                    self.advance()
        except InvalidCoordinateError:
            raise InvalidCoordinateError('Rover position out of plateau grid dimensions')
            pass

    def advance(self):
        """
        Move the rover +1/-1 in x,y Coordinates based on Direction it is heading
        if heading towards N rover move will be from (x,y) to (x,y+1)
        if heading towards N rover move will be from (x,y) to (x,y-1)
        if heading towards E rover move will be from (x,y) to (x,y+1)
        if heading towards W rover move will be from (x,y) to (x,y-1)
        :return: True if rover position is with in the plateau grid dimensions available
        if the rover position is not with in the coordinates raise InvalidCoordinateError exception
        """

        if self.DIRECTIONS['N'] == self._heading:
            self._position.y += 1
        elif self.DIRECTIONS['S'] == self._heading:
            self._position.y -= 1
        elif self.DIRECTIONS['E'] == self._heading:
            self._position.x += 1
        elif self.DIRECTIONS['W'] == self._heading:
            self._position.x -= 1

        if not self._plateau.is_position_within_plateau_area(self._position):
            raise InvalidCoordinateError('Rover position out of plateau grid dimensions')

        return True

    def turn_left(self):
        self._heading = self.DIRECTIONS['W'] if (self._heading - 1) < self.DIRECTIONS['N'] else self._heading - 1

    def turn_right(self):
        self._heading = self.DIRECTIONS['N'] if (self._heading + 1) > self.DIRECTIONS['W'] else self._heading + 1
