from model import *
from view import *
import random
import math


def collision(dt, particles, k):
    for p1 in particles:
        for p2 in particles:
            if p2 != p1:
                r = dot(p1.position, p2.position)

                if r < (p1.radius + p2.radius):
                    F = k * (p1.radius + p2.radius - r)

                    print(F)
                else:
                    print("no force")


if __name__ == "__main__":
    n = 20
    k = 5
    dt = 0.0005


    particles = []


    for i in range(n):
        theta = i * 2 * math.pi / n
        u = Vec(math.cos(theta), math.sin(theta))
        pos = 10 * u
        vel = -1 * u
        rad = random.uniform(0.0, 10.0)
        p = Particle(1, pos, vel, rad)
        charge = random.choice([-5, 5])
        p.set_charge(charge)
        particles.append(p)
    collision(dt, particles, k)