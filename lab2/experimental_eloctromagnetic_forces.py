from view import *
import math
import random

n = 20
particles = []
for i in range(n):
    theta = i*2*math.pi/n
    u = Vec(math.cos(theta),math.sin(theta))
    pos = 10 * u
    vel = -1 * u 
    p = Particle(1,pos,vel,0.2)
    charge = random.uniform(-10,10)
    p.set_charge(charge)
    particles.append(p)

def no_force(dt,particles):
    pass

def coulomb_force(dt, particle, k):
    
    force = ((q1*q2)*k)/(r**2)

def electromagnetic_field(dt, particles, B, mu)


simulation_loop(no_force, 0.000005, particles)
