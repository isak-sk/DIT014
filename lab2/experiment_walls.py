"""
This experiment implements walls so that the particles stays on screen. 
You can either have 4 straight walls as a cube or a circular arena.
k = A spring constant which measures how stiff the wall is
n = A normal vector which points directly away from the wall
a = The point of the wall
x = The position of the particle
"""

from view import * 
from model import combined_walls, circular_walls
import math
import sys


n = 20
particles = []

for i in range(n):
    theta = i*2*math.pi/n
    u = Vec(math.cos(theta),math.sin(theta))
    pos = 5 * u
    vel = -1 * u 
    particles.append(Particle(1,pos,vel,0.2))

# Get user input for what experiment they want to do
try:
    experiment = sys.argv[1]
except IndexError:
    print("Argument not given. Please choose square or circle as first argument")
    sys.exit()


if experiment == ("square"):
    print("Kör experimentet med fyrkantiga väggar")
    simulation_loop(combined_walls, 0.0005, particles)
elif experiment == ("circle"):
    simulation_loop(circular_walls, 0.0005, particles)
    print("Kör experimentet med rund vägg")
else:
    print("Okänt experiment.")