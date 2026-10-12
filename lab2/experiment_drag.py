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


"""
Antagande att partiklarna rör sig på "golvet" och blir tryckta bortfrån skärmen/golvet med gravitationskraft.
"""
def friction(dt, particles, my=0.1, g=9.82):
    for particle in particles:
        velocity = particle.velocity
        vel_norm = velocity.norm()
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


simulation_loop(friktion, 0.001, particles)