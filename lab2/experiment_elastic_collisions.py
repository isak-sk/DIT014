"""
This experiment implements collisions between particles.
It goes through every particle, and for each particle it goes through every particle.
This way every particle can collide with all the others.
It calculates the distance r and if r is less than the 2 radii summed together,
the force is accumalated for all particles and then at the end applied to each particle.
The force is a force vector, meaning its the force * the direction
"""

from model import *
from view import *
import random
import math


def collision(dt, particles, k = 5):
    for p2 in particles:
        total_force = Vec(0, 0)
        for p1 in particles:
            if p2 is not p1:
                distance = p2.position - p1.position

                r = distance.norm()

                if r == 0:
                    continue

                if r < (p1.radius + p2.radius):
                    F = k * (p1.radius + p2.radius - r)
                    direction = (1 / r) * distance
                    force_vector = F * direction
                    total_force += force_vector

        p2.apply_force(dt, total_force)



if __name__ == "__main__":
    n = 20
    dt = 0.0005

    particles = []

    for i in range(n):
        theta = i * 2 * math.pi / n
        u = Vec(math.cos(theta), math.sin(theta))
        pos = 10 * u
        vel = -1 * u
        rad = random.uniform(0.2, 1.2)
        p = Particle(1, pos, vel, rad)
        charge = random.choice([-5, 5])
        p.set_charge(charge)
        particles.append(p)

    simulation_loop(collision, dt, particles)
