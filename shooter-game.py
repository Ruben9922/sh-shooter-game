from sense_hat import SenseHat
from time import sleep
from enum import Enum

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    def multiply_by_scalar(self, scalar):
        self.x *= scalar
        self.y *= scalar

class Position(Vector):
    def __init__(self, x = 0, y = 0, min_x = 0, max_x = 7, min_y = 0, max_y = 7):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        super().__init__(x, y)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if (self.is_x_valid(value)):
            self.__x = value
        else:
            raise ValueError("x-value must be between " + str(self.min_x) + " and " + str(self.max_x) + " inclusive")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if (self.is_y_valid(value)):
            self.__y = value
        else:
            raise ValueError("y-value must be between " + str(self.min_y) + " and " + str(self.max_y) + " inclusive")

    def is_x_valid(self, x):
        return x >= self.min_x and x <= self.max_x

    def is_y_valid(self, y):
        return y >= self.min_y and y <= self.max_y

class GameObject:
    def __init__(self, colour, position, velocity):
        self.colour = colour
        self.position = position
        self.velocity = velocity

    @property
    def position(self):
        return self.__position

    # Setter for position also sets LEDs
    @position.setter
    def position(self, value):
        sense.set_pixel(value.x, value.y, BACKGROUND_COLOUR)
        self.__position = value
        sense.set_pixel(value.x, value.y, self.colour)

sense = SenseHat()
sense.set_rotation(180)
sense.low_light = True

BACKGROUND_COLOUR = [40, 40, 40]

sense.clear(BACKGROUND_COLOUR)
player = GameObject([0, 255, 255], Position(3, 7), Vector(0, 0))

sleep(5)
sense.clear()
sense.low_light = False
