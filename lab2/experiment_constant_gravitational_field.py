#This experiment applies gravity to the particles, pulling them downward, using the formula f = g * m * d
#Where g = 10 (Earth 9.82), m is the particle mass and d is a downward direction vector (0,-1)
#Using the class method apply_force() we can apply the calculated force, which changes the particle velocity
#Because no other forces are applied (like air resistance), the particle mass does not affect the new velocity
#But the previous velocity does.

from model import *
from view import *
import math
import random

#Creating a list of randomized particles
amount = random.randint(1,10)
particles = []

for x in range(amount):
    p_mass = random.randint(1,100)
    p_xpos = random.randint(-10,10)
    p_ypos = random.randint(-10,10)
    p_xvel = random.randint(-10,10)
    p_yvel = random.randint(-10,10)
    p_radius = random.randint(1,2)
    p = Particle(p_mass,Vec(p_xpos,p_ypos),Vec(p_xvel,p_yvel),p_radius)
    particles.append(p) 
    
timestep = 0.000005

#Calling the simulation_loop with this experiment as a parameter
simulation_loop(constant_gravitational_field,timestep,particles)

    
