from marsrover import Plateau
from marsrover import Position
from marsrover import Rover


def main():
    plateau = Plateau(5, 5)
    position = Position(1, 2)
    rover = Rover(plateau, position, Rover.DIRECTIONS.get('N'))
    rover.execute_instructions("LMLMLMLMM")
    #Get the rover position
    print(rover)
    rover.set_position(3, 3, Rover.DIRECTIONS.get('E'))
    rover.execute_instructions("MMRMMRMRRM")
    # Get the rover position
    print(rover)


if __name__ == "__main__":
    main()
