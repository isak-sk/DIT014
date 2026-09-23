from __future__ import annotations
import math


# Task (2/12): Define a class Vec


class Vec:
    def __init__(self, x: float, y: float):
        """
        :param x:  x coordinate of the vector
        :param y:  y coordinate of the vector

        Initialize a new vector at given coords x and y
        """
        self.x: float = x
        self.y: float = y
        self.vector = [x, y]

    def __repr__(self) -> str:
        """
        :return:
        string which is a suitable representation of the vector
        """

        return f"({self.x},{self.y})"

    def __rmul__(self, factor: float) -> Vec:
        """
        :param factor: Factor at which to scale the vector
        :return: New scaled vector

        Return a new vector scaled by the given factor
        """
        new_x: float = self.x * factor
        new_y: float = self.y * factor

        scaled_vector = Vec(new_x, new_y)

        return scaled_vector

    def __add__(self, other: Vec) -> Vec:
        """
        Return a new vector which is the addition of self and other

        :param other: Vector to be added to self
        :return: New vector sum
        """
        x_sum: float = self.x + other.x
        y_sum: float = self.y + other.y

        added_vector = Vec(x_sum, y_sum)

        return added_vector

    def __sub__(self, other: Vec) -> Vec:
        """
        Return a new vector which is the subtraction of self and other

        :param other: Vector to be subtracted from self
        :return: A new vector
        """
        x_sub: float = self.x - other.x
        y_sub: float = self.y - other.y

        subtracted_vector = Vec(x_sub, y_sub)

        return subtracted_vector

    def norm(self) -> float | int:
        """
        Return the euclidian form of self

        :return: The euclidian form of self
        """
        x_squared: float = self.x**2
        y_squared: float = self.y**2
        euclidian_form = math.sqrt(x_squared + y_squared)

        return euclidian_form

    def get_coords(self) -> tuple[float, float]:
        """
        Returns the coordinates of self
        :return: tuple(x,y)
        """
        return self.x, self.y


# Task (3/12): Additionally define a function dot(u, v)


def dot(u: Vec, v: Vec) -> float | int:
    """
    Returns the dot product of two given Vectors

    :param u: first vec object
    :param v: second vec object
    :return: The dot product
    """

    x_prod: float = u.x * v.x
    y_prod: float = u.y * v.y

    dot_product = x_prod + y_prod

    return dot_product


# Task (4/12): Create a class Particle


class Particle:
    def __init__(self, mass: int, position: Vec, velocity: int, radius: float) -> None:
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.x, self.y = position.get_coords()

    def inertial_move(self, dt) -> Vec:
        """
        Modifies the position attribute according the formula:
        (t1 - t0)v + x at time t1
        """
        v = self.velocity
        distans_x = dt * v
        self.position = distans_x + self.position
        return self.position
        
    def apply_force(self, dt, f):
        acceleration = f.__rmul__(self.mass)
        time_force_over_mass = dt * acceleration
        self.velocity = self.velocity + time_force_over_mass
        return self.velocity
# Task (9/12): In the Particle class, add a method bounding_box(self)

    def bounding_box(self):
        """
        Computes the bounding box of a particle
        :return: pair of vectors
        """
        top_left_x = self.x - self.radius
        top_left_y = self.y + self.radius

        bottom_right_x = self.x + self.radius
        bottom_right_y = self.y - self.radius

        upper_left_bound = Vec(top_left_x, top_left_y)
        bottom_right_bound = Vec(bottom_right_x, bottom_right_y)

        return upper_left_bound, bottom_right_bound


###########################################
### When you're done with all 12 tasks: ###
### forces/other features in this file! ###
###########################################
