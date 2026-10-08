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
        self.velocity = self.velocity + (dt * acceleration)
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

def constant_gravitational_field(dt: float, particles: list, g=10):
    "Apply gravitational force on particles"

    #Downward direction vector
    d = Vec(0,-1)

    #Go through every particle, calculate the gravitational force and apply it with the apply_force() method
    for p in particles:
        m = p.mass
        f = g * m * d
        p.apply_force(dt,f)




#Check if the particle is in the wall and calculate force
def wall_force(dt, particles, k, n, a):
    # distance to wall = (x - a)• n
    # force = -kdn
    for particle in particles:
        x = particle.position
        distance = dot(x - a, n)

        if distance < 0:
            force = ((-k) * distance * n)
            particle.apply_force(dt, force)

#Vectors for all 4 walls, check each particle on all 4 walls
def combined_walls(dt, particles):
        walls= [
        (Vec(1, 0), Vec(-8, 0)),
        (Vec(-1, 0), Vec(8, 0)),
        (Vec(0, 1), Vec(0, -8)),
        (Vec(0, -1), Vec(0, 8)),
        ]
        for n, a in walls:
            wall_force(dt, particles, 5, n, a)

#Check if the particle is in the wall and calculates force
#This time with a circular wall
def circular_arena(dt, particles, k, R):
    #f = k * (R - r) * (x / r)
    # = k * ((R - r)/r) * x
    for particle in particles:
        x = particle.position
        r = x.norm()

        if r > R:
            force = k * ((R - r)/ r) * x
            particle.apply_force(dt, force)

#Adds dt an Particles
def circular_walls(dt, Particles):
    circular_arena(dt, Particles, 5, 8)


def coulomb_force(dt, particles, k=(8.99*(10**9))):
     """
    Calculates and applies the elektostatic coulumb forces between all the particels

    Parameters:
    dt (float/int): The time timestep(Delta time) forces are applied
    particles(list): list of the gven particel vectors
    k(float): scoulumbs constant, set to 8.99*(10**9)

    Returns:
    None: Modifies the particle objekts in place
    """
    for particle in particles:
        for other_particle in particles:
            if other_particle != particle:
                q1 = particle.charge
                q2 = other_particle.charge
                lenght = Vec.__sub__(particle.position, other_particle.position)
                r = lenght.norm()
                if r == 0:
                    continue
                if r < 4:
                    r = 4
                normaliserad_form_x = lenght.x / r
                normaliserad_form_y = lenght.y / r
                force = ((q1*q2)*k)/(r**2)
                vec_force_x = normaliserad_form_x * force
                vec_force_y = normaliserad_form_y * force
                vec_force = Vec(vec_force_x, vec_force_y)
                applied_force = particle.apply_force(dt, vec_force)


def electromagnetic_field(dt, particles, B=10, mu=0.1):
    """
    Calculates and applies the magnetic lorenz/electromagnetic field force to all moving particels

    Parameters:
    dt (float): The time timestep(Delta time) the force is applied
    particles(list): list of the given particel vectors
    B(float/int): Megnetic field strenght, set to 10
    mu(float/int): magnetic permability or scaling factor, set to 0.1

    Returns:
    None: Modifies the particle objekts in place

    """
    for particle in particles:
        v_magnitude = particle.velocity.norm()
        if v_magnitude == 0:
            continue
        force = B * mu * particle.charge * v_magnitude
        v_dir_x = particle.velocity.x / v_magnitude
        v_dir_y = particle.velocity.y / v_magnitude
        perpendicular_force = Vec(-v_dir_y*force, v_dir_x*force)
        new_force = particle.apply_force(dt, perpendicular_force)


   
