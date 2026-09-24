from tkinter import *
import math

from view import simulation_loop, root
from model import Particle, Vec

lastPressedKey = None

selected = "all"     # index of the currently controlled particle
mode = "move"     # "move", "accel"

MODES = ["move", "accel"]
MOVE_STEP = 0.5            # distance per keypress
ACCEL_STEP = 2.0           # velocity change per keypress

DIRECTIONS = {
    "Left":  Vec(-1, 0),
    "Right": Vec(1, 0),
    "Up":    Vec(0, 1),
    "Down":  Vec(0, -1),
}


def onKey(event):
    global lastPressedKey
    lastPressedKey = event.keysym

root.bind_all("<Key>", onKey)


def kick(dt, p, direction, amount):
    p.apply_force(dt, (p.mass * amount / dt) * direction)


def bounce(dt, particles, speed=10):
    for p in particles:
        kick(dt, p, Vec(0, 1), speed)

def initial_state(i, n):
    theta = i * 2 * math.pi / n
    u = Vec(math.cos(theta), math.sin(theta))
    return 10 * u, Vec(0, 0)


def reset(particles):
    global selected, mode, angle
    selected = 0
    mode = "move"
    for i, p in enumerate(particles):
        p.position, p.velocity = initial_state(i, len(particles))
    print("Reset")


def handle_key(key, dt, particles):
    global selected, mode, angle

    if key == "x":
        print("Pressed x: exiting")
        exit()

    elif key == "space":
        bounce(dt, particles)

    elif key.isdigit():
        i = int(key)
        if i < len(particles):
            selected = i
            print("Selected particle", i)
        else:
            print("That particle doesn't exist:", i)

    elif key == "a":
        print("selected all particles")
        selected = "all"


    elif key == "m":
        mode = MODES[(MODES.index(mode) + 1) % len(MODES)]
        print("Mode:", mode)

    elif key in DIRECTIONS:

        if selected == "all":
            targets = particles
        else:

            targets = [particles[selected]]

        for p in targets:
            if mode == "move":
                p.position = p.position + MOVE_STEP * DIRECTIONS[key]

            elif mode == "accel":
                kick(dt, p, DIRECTIONS[key], ACCEL_STEP)


    elif key == "r":
        print("RESETING PARTICLES")
        reset(particles)

    else:
        print("Other key:", key)


def step(dt, particles):
    global lastPressedKey

    key = lastPressedKey
    lastPressedKey = None
    if key is not None:
        handle_key(key, dt, particles)

    # Gravity
    #for p in particles:
    #    p.apply_force(dt, Vec(0, -9.81 * p.mass))

def no_force(dt, particles):
    pass


CONTROLS_TEXT = """\
Controls

0-9      select particle
a        select all particles
m        switch mode (move / accel)
Arrows   move: shift position
         accel: change velocity
space    bounce all particles up
r        reset to initial state
x        quit
"""

def show_controls():
    win = Toplevel(root)
    win.title("Controls")
    Label(win, text=CONTROLS_TEXT, font=("Courier", 11),
          justify=LEFT, padx=15, pady=10).pack()

if __name__ == "__main__":
    n = 10
    particles = []
    for i in range(n):
        pos, vel = initial_state(i, n)
        particles.append(Particle(1, pos, vel, 0.2))

    show_controls()
    simulation_loop(step, 0.000005, particles)