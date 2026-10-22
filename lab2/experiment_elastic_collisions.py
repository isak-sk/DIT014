"""
This experiment implements collisions between particles.
It goes through every particle, and for each particle it goes through every particle.
This way every particle can collide with all the others.
It calculates the distance r and if r is less than the 2 radii summed together,
the force is accumalated for all particles and then at the end applied to each particle.
The force is a force vector, meaning its the force * the direction
"""

from model import collision, Vec, Particle
from view import simulation_loop
import random
import math





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
