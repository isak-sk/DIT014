from model import *
from tkinter import *
import time






# Helper function for walls in other files
def reflect(pos: float, vel: float, limit: float):
    if pos < -limit:
        return -limit, abs(vel)
    if pos > limit:
        return limit, -abs(vel)
    return pos, vel


def keep_particles_inside_arena(particles):
    for p in particles:
        x, vx = reflect(p.position.x, p.velocity.x, 10)
        y, vy = reflect(p.position.y, p.velocity.y, 8)
        p.position = Vec(x, y)
        p.velocity = Vec(vx, vy)

        print(p.position)
        print(p.velocity)



# Task (7/12): Draw on canvas
root = Tk()
canvas = Canvas(root, bg="white", width=800, height=600)
canvas.pack()


# Task (8/12): Define a new function to_canvas_coords(canvas, x)
def to_canvas_coords(canvas, u: Vec):

    height = canvas.winfo_reqheight()
    width = canvas.winfo_reqwidth()
    scaling_factor = (height / 20)
    sim_x, sim_y = u.get_coords()

    # Invert y axis
    canvas_y = sim_y * -1

    # translate to (0, 0)
    canvas_x = (sim_x * scaling_factor) + (width / 2)
    canvas_y = (canvas_y * scaling_factor) + (height / 2)

    canvas_vec = Vec(canvas_x, canvas_y)

    return canvas_vec


#######################################
### NB. Task 9 is done in model.py. ###
#######################################

# Task (10/12): Define a new function move_oval_to(o, u1, u2)
def move_oval_to(canvas, o, u1: Vec, u2: Vec):

    coordinates_u1 = to_canvas_coords(canvas, u1)
    coordinates_u2 = to_canvas_coords(canvas, u2)
    x1, y1 = coordinates_u1.get_coords()
    x2, y2 = coordinates_u2.get_coords()

    oval = canvas.coords(o, x1, y1, x2, y2)

    return oval

# Task (11/12): Define a new function create_oval(canvas, particle)

def create_oval(canvas, particle: Particle):

    max_charge = 10

    ratio =((particle.charge)/max_charge)

    charge_ratio = min(abs(ratio), 1.0)

    intensity = int(charge_ratio*255)

    if particle.charge > 0:
        particle_color = f"#0000{intensity:02x}"

    elif particle.charge < 0:
        particle_color = f"#ff00{intensity:02x}"

    else:
        particle_color = f"#808080"

    u1, u2 = particle.bounding_box()

    o = canvas.create_oval(80, 30, 140, 150, fill=particle_color)

    move_oval_to(canvas, o, u1, u2)

    return o

# Task (12/12): Define a function simulation_loop(f, timestep, particles)

def simulation_loop(f, timestep, particles):

    ovals = [create_oval(canvas, p) for p in particles]
    canvas.update()

    interval = 1 / 30
    last_update = time.time()

    while True:
        f(timestep, particles)
        keep_particles_inside_arena(particles)

        for p in particles:
            p.inertial_move(timestep)

        now = time.time()
        if now - last_update >= interval:
            for p, o in zip(particles, ovals):
                vec1, vec2 = p.bounding_box()
                move_oval_to(canvas, o, vec1, vec2)
            canvas.update()
            last_update = now

