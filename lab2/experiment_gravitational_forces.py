#This experiment implements gravitational forces between all particles. To demonstrate it we have have a high mass
#particle in the middle and two lighter particles on the outide with starting velocitites upward/downward.
#The combination of the gravitational forces pulling the lighter particles toward the middle and their starting
#velocities, will create an orbit.

from model import *
from view import *

def gravitational_force(dt: float, particles: list[Particle], G=150):
    "For each particle, calculate the gravitational force exerted by every other particle, and apply the accumulated force on the particle"
    
    #Loop through every particle
    for p2 in particles:

        #Force vector where the forces will be accumulated
        F_total = Vec(0,0)
        
        #Loop through every other particle
        for p1 in particles:

            #Skip itself
            if p1 is p2:
                continue
            
            m1 = p1.mass
            m2 = p2.mass

            #Difference vector
            r_vec = p1.position - p2.position

            #Length of the differnce vector; distance between the two particles
            r = r_vec.norm()

            #Avoid division by zero
            if r == 0:
                continue

            #Direction vector
            direction = Vec(r_vec.x / r, r_vec.y / r)

            #Calculate the force
            F = (G*m1*m2)/(r**2)

            #Multiply it with the direction vector
            F2 = F * direction

            #Add it to total
            F_total = F_total + F2

        #Apply to the total force to the particle
        p2.apply_force(dt,F_total)


p1 = Particle(100,Vec(0,0),Vec(0,0),1)
p2 = Particle(1,Vec(10,0),Vec(0,30),0.4)
p3 = Particle(1,Vec(-10,0),Vec(0,-30),0.4)
particles = [p1,p2,p3]

timestep = 0.00005

simulation_loop(gravitational_force, timestep, particles)


