"""
This experiment implements walls so that the particles stays on screen. 
You can either have 4 straight walls as a cube or a circular arena.
k = A spring constant which measures how stiff the wall is
n = A normal vector which points directly away from the wall
a = The point of the wall
x = The position of the particle
"""

from view import * 
from model import *
import math
import sys

#Check if the particle is in the wall and calculate force
def wall_force(dt, particles, k, n, a):
    # distance to wall = (x - a)• n
    # force = -kdn
    for particle in particles:
        x = particle.position
        distance = dot(x - a, n)

        if distance < 0:
            force = ((-k) * distance * n)
            particle.apply_force(dt, force)

#Vectors for all 4 walls, check each particle on all 4 walls
def combined_walls(dt, particles):
        walls= [
        (Vec(1, 0), Vec(-8, 0)), 
        (Vec(-1, 0), Vec(8, 0)),
        (Vec(0, 1), Vec(0, -8)),
        (Vec(0, -1), Vec(0, 8)),
        ] 
        for n, a in walls:
            wall_force(dt, particles, 5, n, a)  

#Check if the particle is in the wall and calculates force
#This time with a circular wall
def circular_arena(dt, particles, k, R):
    #f = k * (R - r) * (x / r)
    # = k * ((R - r)/r) * x
    for particle in particles:
        x = particle.position
        r = x.norm()

        if r > R:
            force = k * ((R - r)/ r) * x
            particle.apply_force(dt, force)     

#Adds dt an Particles
def circular_walls(dt, Particles):
    circular_arena(dt, particles, 5, 8)


n = 20
particles = []

for i in range(n):
    theta = i*2*math.pi/n
    u = Vec(math.cos(theta),math.sin(theta))
    pos = 5 * u
    vel = -1 * u 
    particles.append(Particle(1,pos,vel,0.2))

# Get user input for what experiment they want to do
experiment = sys.argv[1]

if experiment == ("square"):
    print("Kör experimentet med fyrkantiga väggar")
    simulation_loop(combined_walls, 0.0005, particles)
elif experiment == ("circle"):
    simulation_loop(circular_walls, 0.0005, particles)
    print("Kör experimentet med rund vägg")
else:
    print("Okänt experiment.")