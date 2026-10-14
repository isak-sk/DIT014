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


def vanderwaals_force(dt, particles, A):
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


# Creates particles
n = 16
particles = []

for i in range(n):
    theta = i * 2 * math.pi / n
    u = Vec(math.cos(theta), math.sin(theta))
    pos = 6 * u
    vel = Vec(0, 0)
    radius = 0.2 + 0.1 * (i % 4)
    p = Particle(1, pos, vel, radius)
    charge = random.choice([-5, 5])
    p.set_charge(charge)

    particles.append(p)


# Apply the force at each simulation step
def experiment(dt, particles):
    vanderwaals_force(dt, particles, 100)


# Change this value to compare different time steps
timestep = 0.0005

simulation_loop(experiment, timestep, particles)

