from model import *
from tkinter import *

# Task (7/12): Draw on canvas
root = Tk()
canvas = Canvas(root, bg="white", width=800, height=600)
canvas.pack()
o = canvas.create_oval(80, 30, 140, 150, fill='purple')

input()

# Task (8/12): Define a new function to_canvas_coords(canvas, x)


def to_canvas_coord(canvas, u):


    height = canvas.winfo_reqheight()
    width = canvas.winfo_reqwidth()
    scaling_factor = (height / 20)
    sim_x = u[0]
    sim_y = u[1]

    canvas_vector = Vec(sim_x, sim_y)






#######################################
### NB. Task 9 is done in model.py. ###
#######################################

# Task (10/12): Define a new function move_oval_to(o, u1, u2)

# Task (11/12): Define a new function create_oval(canvas, particle)

# Task (12/12): Define a function simulation_loop(f, timestep, particles)