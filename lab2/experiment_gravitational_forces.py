# This experiment implements gravitational forces between all particles. To demonstrate it we have have a high mass
# particle in the middle and two lighter particles on the outide with starting velocitites upward/downward.
# The combination of the gravitational forces pulling the lighter particles toward the middle and their starting
# velocities, will create an orbit.

from model import gravitational_force
from view import *



p1 = Particle(100, Vec(0, 0), Vec(0, 0), 1)
p2 = Particle(1, Vec(10, 0), Vec(0, 30), 0.4)
p3 = Particle(1, Vec(-10, 0), Vec(0, -30), 0.4)
particles = [p1, p2, p3]

timestep = 0.000005

simulation_loop(gravitational_force, timestep, particles)
