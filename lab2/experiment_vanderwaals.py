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

import math
from model import Particle, Vec
from view import simulation_loop
import random


def vanderwaals_force(dt, particles, A = 100):
    for p2 in particles:
        total_force = Vec(0, 0)

        for p1 in particles:
            if p1 is not p2:
                direction = p1.position - p2.position
                length = direction.norm()

                if length != 0:
                    R1 = p1.radius
                    R2 = p2.radius

                    F = (A * R1 * R2) / (6 * (R1 + R2) * length**2)
                    unit_direction = (1 / length) * direction

                    total_force = total_force + F * unit_direction

        # Apply the accumulated force
        p2.apply_force(dt, total_force)



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

