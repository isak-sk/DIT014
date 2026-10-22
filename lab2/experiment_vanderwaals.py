"""
experiment_vanderwaals.py

Demonstrates van der Waals attraction: particles pull towards each
other with a force that becomes stronger as the distance decreases.

vanderwaals_force  adds up the forces on each particle and updates its velocity
A                 controls the strength of the attraction
timestep          simulated time per calculation step
mass              particle mass; higher mass means less acceleration
radius            particle size; also affects the attraction
position          particle's starting coordinates
velocity          particle's starting speed and direction
"""

from model import Particle, Vec, vanderwaals_force
from view import simulation_loop





p1 = Particle(1, Vec(-5, 5), Vec(1, -1), 0.5)
p1.set_charge(5)

p2 = Particle(1, Vec(-5, -5), Vec(1, 1), 0.5)
p2.set_charge(-5)

p3 = Particle(1, Vec(5, 5), Vec(-1, -1), 0.5)
p3.set_charge(5)

p4 = Particle(1, Vec(5, -5), Vec(-1,1),0.5)
p4.set_charge(-5)


particles = [p1,p2,p3,p4]



# Change this value to compare different time steps
timestep = 0.00001

simulation_loop(vanderwaals_force, timestep, particles)

