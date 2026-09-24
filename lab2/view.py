from model import *
from tkinter import *
import time

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

    u1, u2 = Particle.bounding_box(particle)

    o = canvas.create_oval(80, 30, 140, 150, fill='purple')

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

        for p in particles:
            p.inertial_move(timestep)

        now = time.time()
        if now - last_update >= interval:
            for p, o in zip(particles, ovals):
                vec1, vec2 = p.bounding_box()
                move_oval_to(canvas, o, vec1, vec2)
            canvas.update()
            last_update = now

