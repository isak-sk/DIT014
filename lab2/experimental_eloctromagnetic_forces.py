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

def coulomb_force(dt, particles, k=(8.99*(10**9))):
    for particle in particles:
        for other_particle in particles:
            if other_particle != particle:
                q1 = particle.charge
                q2 = other_particle.charge
                lenght = Vec.__sub__(particle.position, other_particle.position)
                r = abs(lenght.norm())
                if r == 0:
                    continue
                if r < 5:
                    r = 5
                normaliserad_form_x = lenght.x / r
                normaliserad_form_y = lenght.y / r
                force = ((q1*q2)*k)/(r**2)
                vec_force_x = normaliserad_form_x * force
                vec_force_y = normaliserad_form_y * force
                vec_force = Vec(vec_force_x, vec_force_y)
                particle.apply_force(dt, vec_force)
                


def electromagnetic_field(dt, particles, B, mu):
    pass


simulation_loop(coulomb_force, 0.000005, particles)

#simulation_loop(no_force, 0.000005, particles)

