from view import *
import math
import random
import sys


#experiment = sys.argv[1]


n = 20
particles = []
for i in range(n):
    theta = i * 2 * math.pi / n
    u = Vec(math.cos(theta),math.sin(theta))
    pos = 10 * u
    vel = -10 * u
    p = Particle(1 , pos , vel ,0.2)
    charge = random.choice([-5,5])
    p.set_charge(charge)
    particles.append(p)


"""
Antagande att partiklarna rör sig på "golvet" och blir tryckta bortfrån skärmen/golvet med gravitationskraft.
"""
def friktion(dt, particles, my_rörelse=0.509, g=9.82):
    for particle in particles:
        velocity = particle.velocity
        vel_norm = velocity.norm()
        my = my_rörelse
        if vel_norm == 0:
            continue
        m = particle.mass
        normal_force = m * g
        friktion = normal_force * my
        t0_force = (vel_norm * m)/dt
        if friktion > t0_force:
            friktion = t0_force
        force_x = -friktion* (velocity.x/vel_norm)
        force_y = -friktion* (velocity.y/vel_norm)
        friktion_force = Vec(force_x, force_y)
        particle.apply_force(dt, friktion_force)



def drag(dt, particles, p=1.225, cd=0.47):
    for particle in particles:
        area = particle.radiuse2 * math.pi
        force = (1/2) * area * p * cd * particle.velocity.norm
        if force == 0:
            continue
        