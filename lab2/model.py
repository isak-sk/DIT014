from __future__ import annotations
import math


# Task (2/12): Define a class Vec


class Vec:
    def __init__(self, x: float, y: float) -> None:
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
        x_sum: float | int = self.x + other.x
        y_sum: float | int = self.y + other.y

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
    def __init__(self, mass: int, position: Vec, velocity: Vec, radius: float) -> None:
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.charge = 0

# Task (5/12): In the Particle class, implement a method inertial_move(self, dt).
    def inertial_move(self, dt: float) -> Vec:
        """
        Modifies the position attribute according the formula:
        (x, y) = dt * v + x0 at time t1
        
        parmeters: 
        dt (float): The time step(Delta t) it took to move the particle forward

        Returns:
        Vec: The updated position Vector with x and y coordinates
        """
        distance_x = dt * self.velocity
        self.position = distance_x + self.position

        return self.position
        

# Task (6/12): In the Particle class, implement a method apply_force(self, dt, f)
    def apply_force(self, dt: float, f: Vec):
        """
        Modifies the velocity attribute according to the formula:
        v1 = dt * (f / m) + v0

        Parameters:
        dt (float): The time step (delta time) the force is applied
        f (Vec): The applied force vector on the particle

        Returns:
        Vec: The updated velocity vector with new x and y coordinates
        """
        acceleration = (1 / self.mass) * f
        self.velocity = self.velocity + dt * acceleration

        return self.velocity



# Task (9/12): In the Particle class, add a method bounding_box(self)

    def bounding_box(self):
        """
        Computes the bounding box of a particle
        :return: pair of vectors
        """

        x, y = self.position.get_coords()

        upper_left_bound = Vec(x - self.radius, y + self.radius)
        bottom_right_bound = Vec(x + self.radius, y - self.radius)

        return upper_left_bound, bottom_right_bound

    

# experimental electromagnetic forces:
    def set_charge(self, new_charge: float):
        self.charge = new_charge




###########################################
### When you're done with all 12 tasks: ###
### forces/other features in this file! ###
###########################################
