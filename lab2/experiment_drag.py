"""
In this experiment we want to showcase how both drag and friktion can be implemented on the particels and how they would react.
The particles should slow down until the reach a complet stop if no outside forces are applied.

the given experiment did what we thought it would. The particels slow down depending on the given timestep, velocity and forces.
"""


from view import simulation_loop
import math
import random
import sys
from model import friktion, drag, Vec, Particle



try:
    experiment = sys.argv[1]
except IndexError:
    print("Argument not given. Please choose drag or friction as first argument")
    sys.exit()


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


if experiment == "friction":
    """
    Antagande att partiklarna rör sig på "golvet" och blir tryckta bortfrån skärmen/golvet med gravitationskraft.
    """
    simulation_loop(friktion, 0.000005, particles)

elif experiment == "drag":
    simulation_loop(drag, 0.00005, particles)

else:
    print("Unknown experiment")
    sys.exit()