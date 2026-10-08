from view import *
import math
import random
import sys




experiment = sys.argv[1]




n = 20
particles = []
for i in range(n):
    theta = i * 2 * math.pi / n
    u = Vec(math.cos(theta),math.sin(theta))
    pos = 10 * u
    vel = -1 * u
    p = Particle(1 , pos , vel ,0.2)
    charge = random.choice([-5,5])
    p.set_charge(charge)
    particles.append(p)

def no_force(dt,particles):
    pass

def coulomb_force(dt, particles, k=(8.99*(10**9))):
     """
    Calculates and applies the elektostatic coulumb forces between all the particels

    Parameters:
    dt (float/int): The time timestep(Delta time) forces are applied
    particles(list): list of the gven particel vectors
    k(float): scoulumbs constant, set to 8.99*(10**9)

    Returns:
    None: Modifies the particle objekts in place

   """
    for particle in particles:
        for other_particle in particles:
            if other_particle != particle:
                q1 = particle.charge
                q2 = other_particle.charge
                lenght = Vec.__sub__(particle.position, other_particle.position)
                r = lenght.norm()
                if r == 0:
                    continue
                if r < 4:
                    r = 4
                normaliserad_form_x = lenght.x / r
                normaliserad_form_y = lenght.y / r
                force = ((q1*q2)*k)/(r**2)
                vec_force_x = normaliserad_form_x * force
                vec_force_y = normaliserad_form_y * force
                vec_force = Vec(vec_force_x, vec_force_y)
                applied_force = particle.apply_force(dt, vec_force)


def electromagnetic_field(dt, particles, B=10, mu=0.1):
    """
    Calculates and applies the magnetic lorenz/electromagnetic field force to all moving particels

    Parameters:
    dt (float): The time timestep(Delta time) the force is applied
    particles(list): list of the given particel vectors
    B(float/int): Megnetic field strenght, set to 10
    mu(float/int): magnetic permability or scaling factor, set to 0.1

    Returns:
    None: Modifies the particle objekts in place

    """
    for particle in particles:
        v_magnitude = particle.velocity.norm()
        if v_magnitude == 0:
            continue
        force = B * mu * particle.charge * v_magnitude
        v_dir_x = particle.velocity.x / v_magnitude
        v_dir_y = particle.velocity.y / v_magnitude
        perpendicular_force = Vec(-v_dir_y*force, v_dir_x*force)
        new_force =  particle.apply_force(dt, perpendicular_force)


if experiment == "electro":

    simulation_loop(electromagnetic_field, 0.001, particles)

elif experiment == "coulomb":

    simulation_loop(coulomb_force, 0.00000005, particles)

else:
    print("Unknown experiment")
    sys.exit()


