class InvalidCoordinateError(BaseException):
    def __init__(self, errmsg):
        if errmsg:
            print(errmsg)
        pass

class InvalidDirectionError(BaseException):
    def __init__(self, errmsg):
        if errmsg:
            print(errmsg)
        pass


class Plateau(object):
    MIN_WIDTH = 0
    MIN_HEIGHT = 0

    def __init__(self, width, height, min_width=0, min_height=0):
        self.width = width
        self.height = height
        self.MIN_WIDTH = min_width
        self.MIN_HEIGHT = min_height


    def is_position_within_plateau_area(self, position):
        """
        Check if rover move is valid
        :param Position position:
        :return: True if valid coordinates available for rover to advance
        """
        return self.MIN_WIDTH <= position.x <= self.width and self.MIN_HEIGHT <= position.y <= self.height
