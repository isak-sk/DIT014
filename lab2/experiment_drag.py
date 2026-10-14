"""
In this experiment we want to showcase how both drag and friktion can be implemented on the particels and how they would react.
The particles should slow down until the reach a complet stop if no outside forces are applied.

the given experiment did what we thought it would. The particels slow down depending on the given timestep, velocity and forces.
"""







from view import *
import math
import random
import sys


# experiment = sys.argv[1]


n = 10
particles = []
for i in range(n):
    theta = i * 2 * math.pi / n
    u = Vec(math.cos(theta), math.sin(theta))
    pos = 10 * u
    vel = -100 * u
    p = Particle(1, pos, vel, 0.2)
    charge = random.choice([-1, 1])
    p.set_charge(charge)
    particles.append(p)


"""
Antagande att partiklarna rör sig på "golvet" och blir tryckta bortfrån skärmen/golvet med gravitationskraft.
"""


def friktion(dt, particles, my=0.509, g=9.82):
    """
    Calculates and applies friktion on all the particles by a set gravitational force and frictions constant.

    Parameters:
    dt (float/int): The time timestep (Delta time) over which forces are applied.
    particles (list): List of the given particle vectors
    my (float): friction constant, set to 0.509
    g (float): Gravitational constant, set as 9.82, the standard in Sweden.

    Returns:
    None: Modifies the particle objects in place
    """
    for particle in particles:
        velocity = particle.velocity
        vel_norm = velocity.norm()
        # Divide by 10 because speed is to fast.
        vel_norm = vel_norm / 10
        if vel_norm == 0:
            continue
        m = particle.mass
        normal_force = m * g
        friktion = normal_force * my
        t0_force = (vel_norm * m) / dt
        if friktion > t0_force:
            friktion = t0_force
        force_x = -friktion * (velocity.x / vel_norm)
        force_y = -friktion * (velocity.y / vel_norm)
        friktion_force = Vec(force_x, force_y)
        particle.apply_force(dt, friktion_force)


def drag(dt, particles, p=1.225, cd=0.47):
    """
    Calculates and applies drag on all the particles by a set mass density and drag constant.

    Parameters:
    dt (float/int): The timestep (Delta time) over which forces are applied.
    particles (list): List of the given particle vectors
    p (float): The Mass density, set to 1.225 for the density of air
    cd (float): The drag coefficient, set to 0.47.

    Returns:
    None: Modifies the particle objekts in place
    """
    for particle in particles:
        area = particle.radius**2 * math.pi
        vel_norm = particle.velocity.norm()
        if vel_norm == 0:
            continue
        m = particle.mass
        drag = (1 / 2) * area * p * cd * (vel_norm**2)
        t0_force = (vel_norm * m) / dt
        if drag > t0_force:
            drag = t0_force
        force_x = -drag * (particle.velocity.x / vel_norm)
        force_y = -drag * (particle.velocity.y / vel_norm)
        drag_force = Vec(force_x, force_y)
        particle.apply_force(dt, drag_force)


simulation_loop(friktion, 0.000005, particles)
