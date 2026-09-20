import math
from typing import List

# Task (2/12): Define a class Vec

class Vec:


    def __init__(self, x: int, y: int):
        """
        :param x:  x coordinate of the vector
        :param y:  y coordinate of the vector

        Initialize a new vector at given coords x and y
        """
        self.x = x
        self.y = y
        self.vector = [x, y]


    def __repr__(self) -> str:
        """
        :return:
        string which is a suitable representation of the vector
        """

        return f"({self.x},{self.y})"

    def __rmul__(self, factor) -> List[int]:
        """
        :param factor: Factor at which to scale the vector
        :return: New scaled vector

        Return a new vector scaled by the given factor
        """
        new_x: int = self.x * factor
        new_y: int = self.y * factor

        scaled_vector = [new_x, new_y]

        return scaled_vector

    def __add__(self, other):
        """
        Return a new vector which is the addition of self and other

        :param other: Vector to be added to self
        :return: New vector sum
        """
        x_sum = self.x + other[0]
        y_sum = self.y + other[1]

        return [x_sum, y_sum]



# Task (3/12): Additionally define a function dot(u, v)

# Task (4/12): Create a class Particle

# Task (5/12): In the Particle class, implement a method inertial_move(self, dt).

# Task (6/12): In the Particle class, implement a method apply_force(self, dt, f)

##########################################
### NB. Tasks 7–8 are done in view.py. ###
##########################################


# Task (9/12): In the Particle class, add a method bounding_box(self)






###########################################
### When you're done with all 12 tasks: ###
### forces/other features in this file! ###
###########################################