"""
experiment_game.py

Exactly one particle is yellow: that is the one is controlled by the player. The rest are purple.

  Arrow keys / WASD   push the yellow particle in that direction
  0-9                 choose which particle you control (0 = first particle)
  M                   switch between "accel" (push, with drag) and "move" (direct step)
  SPACE               kick every particle upward
  P                   pause / unpause
  R                   restart
  ESC                 quit

Goal: touch the green circle for points. Touching a purple particle costs a life.
"""



import math
import random
import sys
import time
from tkinter import Toplevel, Label, LEFT

from view import simulation_loop, root, canvas, to_canvas_coords
from model import Particle, Vec


NUM_PARTICLES = 10
TIMESTEP = 1 / 120

ARENA_W = 13.0
ARENA_H = 9.5

PLAYER_ACCELERATION = 25.0
PLAYER_DRAG = 2.5
PLAYER_MOVE_SPEED = 8.0
PARTICLE_RADIUS = 0.3

GOAL_RADIUS = 1.0
GOAL_MIN_DISTANCE = 4.0
ENEMY_SPEED = (2.0, 5.0)
INVULNERABLE_TIME = 1.5
STARTING_LIVES = 3


def distance(a: Vec, b: Vec) -> float:
    return (a - b).norm()


def random_position() -> Vec:
    return Vec(
        random.uniform(-ARENA_W + 1, ARENA_W - 1),
        random.uniform(-ARENA_H + 1, ARENA_H - 1),
    )


def initial_state(i: int, n: int):
    theta = i * 2 * math.pi / n
    position = 8 * Vec(math.cos(theta), math.sin(theta))

    if i == 0:
        velocity = Vec(0, 0)
    else:
        speed = random.uniform(*ENEMY_SPEED)
        angle = random.uniform(0, 2 * math.pi)
        velocity = speed * Vec(math.cos(angle), math.sin(angle))

    return position, velocity


def create_particles(n: int):
    particles = []
    for i in range(n):
        position, velocity = initial_state(i, n)
        particles.append(Particle(1, position, velocity, PARTICLE_RADIUS))
    return particles


def reflect(pos: float, vel: float, limit: float):
    if pos < -limit:
        return -limit, abs(vel)
    if pos > limit:
        return limit, -abs(vel)
    return pos, vel


class GameState:
    def __init__(self):
        self.reset()

    def reset(self):
        self.score = 0
        self.lives = STARTING_LIVES
        self.paused = False
        self.game_over = False
        self.mode = "accel"
        self.time = 0.0
        self.invulnerable_until = 0.0


class Goal:
    def __init__(self):
        self.radius = GOAL_RADIUS
        self.position = random_position()

    def relocate(self, avoid: Vec):
        while True:
            self.position = random_position()
            if distance(self.position, avoid) > GOAL_MIN_DISTANCE:
                break


class InputHandler:
    def __init__(self, root):
        self.keys = set()
        root.bind_all("<KeyPress>", self.key_down)
        root.bind_all("<KeyRelease>", self.key_up)
        root.bind_all("<FocusOut>", lambda e: self.keys.clear())

    def key_down(self, event):
        self.keys.add(event.keysym.lower())

    def key_up(self, event):
        self.keys.discard(event.keysym.lower())

    def pressed(self, key):
        return key.lower() in self.keys


class Game:
    def __init__(self, particles):
        self.particles = particles
        self.state = GameState()
        self.input = InputHandler(root)

        self.player = particles[0]
        self.goal = Goal()
        self.goal.relocate(self.player.position)

        self.message = "Reach the green goal!"
        self.previous_keys = set()
        self.saved_velocities = None
        self.next_tick = None
        self.frame = 0


        tl = to_canvas_coords(canvas, Vec(-ARENA_W, ARENA_H)).get_coords()
        br = to_canvas_coords(canvas, Vec(ARENA_W, -ARENA_H)).get_coords()
        arena = canvas.create_rectangle(*tl, *br, outline="gray")
        self.goal_oval = canvas.create_oval(0, 0, 0, 0, fill="green", outline="")
        self.hud = canvas.create_text(
            10, 10, anchor="nw", font=("Courier", 12), text=""
        )
        self.own_items = {arena, self.goal_oval, self.hud}

    @property
    def enemies(self):
        return [p for p in self.particles if p is not self.player]


    def throttle(self):
        now = time.perf_counter()
        if self.next_tick is None:
            self.next_tick = now
        self.next_tick += TIMESTEP
        delay = self.next_tick - now
        if delay > 0:
            time.sleep(delay)
        elif delay < -0.1:
            self.next_tick = now


    def freeze(self):
        for p in self.particles:
            p.velocity = Vec(0, 0)

    def set_paused(self, paused: bool):
        if paused == self.state.paused:
            return
        self.state.paused = paused
        if paused:
            self.saved_velocities = [p.velocity for p in self.particles]
            self.freeze()
            self.message = "PAUSED"
        else:
            if self.saved_velocities:
                for p, v in zip(self.particles, self.saved_velocities):
                    p.velocity = v
            self.saved_velocities = None
            self.message = "Go!"


    def pressed_once(self, key):
        key = key.lower()
        return self.input.pressed(key) and key not in self.previous_keys

    def handle_commands(self):
        if self.pressed_once("escape"):
            self.quit()

        if self.pressed_once("r"):
            self.reset()
            return

        if self.state.game_over:
            return

        if self.pressed_once("p"):
            self.set_paused(not self.state.paused)

        if self.state.paused:
            return

        if self.pressed_once("m"):
            self.state.mode = "move" if self.state.mode == "accel" else "accel"
            self.message = f"Mode: {self.state.mode}"

        if self.pressed_once("space"):
            for p in self.particles:
                p.velocity = p.velocity + Vec(0, 10)

        for i in range(min(10, len(self.particles))):
            if self.pressed_once(str(i)):
                self.player = self.particles[i]
                self.state.invulnerable_until = self.state.time + 1.0
                self.message = f"Controlling particle {i}"

    def handle_player_input(self, dt):
        direction = Vec(0, 0)
        if self.input.pressed("left") or self.input.pressed("a"):
            direction = direction + Vec(-1, 0)
        if self.input.pressed("right") or self.input.pressed("d"):
            direction = direction + Vec(1, 0)
        if self.input.pressed("up") or self.input.pressed("w"):
            direction = direction + Vec(0, 1)
        if self.input.pressed("down") or self.input.pressed("s"):
            direction = direction + Vec(0, -1)

        if self.state.mode == "move":
            self.player.velocity = Vec(0, 0)

        length = direction.norm()
        if length == 0:
            return
        direction = (1 / length) * direction

        if self.state.mode == "move":
            self.player.position = (
                self.player.position + (PLAYER_MOVE_SPEED * dt) * direction
            )
        else:
            self.player.apply_force(
                dt, (self.player.mass * PLAYER_ACCELERATION) * direction
            )


    def check_goal(self):
        if distance(self.player.position, self.goal.position) < self.goal.radius:
            self.state.score += 1
            self.message = f"Goal! Score: {self.state.score}"
            self.goal.relocate(self.player.position)

    def check_enemy_collision(self):
        if self.state.time < self.state.invulnerable_until:
            return

        for enemy in self.enemies:
            hit = self.player.radius + enemy.radius
            if distance(self.player.position, enemy.position) < hit:
                self.state.lives -= 1
                self.player.position = Vec(0, 0)
                self.player.velocity = Vec(0, 0)
                self.state.invulnerable_until = self.state.time + INVULNERABLE_TIME

                if self.state.lives <= 0:
                    self.state.game_over = True
                    self.freeze()
                    self.message = "GAME OVER - press R"
                else:
                    self.message = f"Hit! {self.state.lives} lives left"
                break

    def keep_particles_inside_arena(self):
        for p in self.particles:
            x, vx = reflect(p.position.x, p.velocity.x, ARENA_W)
            y, vy = reflect(p.position.y, p.velocity.y, ARENA_H)
            p.position = Vec(x, y)
            p.velocity = Vec(vx, vy)

    def reset(self):
        self.state.reset()
        self.saved_velocities = None
        n = len(self.particles)
        for i, p in enumerate(self.particles):
            p.position, p.velocity = initial_state(i, n)
        self.player = self.particles[0]
        self.goal.relocate(self.player.position)
        self.message = "Reach the green goal!"


    def draw(self):
        ovals = [i for i in canvas.find_all() if i not in self.own_items]
        blink_off = (
            self.state.time < self.state.invulnerable_until
            and int(self.state.time * 8) % 2 == 0
        )

        for p, o in zip(self.particles, ovals):
            if p is self.player:
                color = "#ffffb0" if blink_off else "yellow"
            else:
                color = "purple"
            canvas.itemconfig(o, fill=color)

        r = self.goal.radius
        g = self.goal.position
        x1, y1 = to_canvas_coords(canvas, g + Vec(-r, r)).get_coords()
        x2, y2 = to_canvas_coords(canvas, g + Vec(r, -r)).get_coords()
        canvas.coords(self.goal_oval, x1, y1, x2, y2)

        canvas.itemconfig(
            self.hud,
            text=(
                f"Score: {self.state.score}   Lives: {self.state.lives}   "
                f"Mode: {self.state.mode}\n{self.message}"
            ),
        )
        canvas.tag_raise(self.hud)


    def update(self, dt, particles):
        self.throttle()
        self.handle_commands()

        if self.state.paused or self.state.game_over:
            self.freeze()
        else:
            self.state.time += dt
            self.handle_player_input(dt)

            v = self.player.velocity
            self.player.velocity = (1 - PLAYER_DRAG * dt) * v

            self.keep_particles_inside_arena()
            self.check_goal()
            self.check_enemy_collision()

        self.frame += 1
        if self.frame % 4 == 0:
            self.draw()

        self.previous_keys = set(self.input.keys)

    def show_controls(self):
        win = Toplevel(root)
        win.title("Particle Arena Game")

        text = """
PARTICLE ARENA GAME
==============

Reach the green goal as many times as possible, avoid the purple particles.

MOVEMENT
--------
WASD / Arrow keys

GAME
----
P       pause
R       restart
ESC     quit

MODE
----
M       move / acceleration

PARTICLES
---------
0-9     control particle

OTHER
-----
SPACE   bounce all particles
"""
        Label(
            win, text=text, font=("Courier", 11), justify=LEFT, padx=15, pady=10
        ).pack()
        root.focus_force()

    def quit(self):
        root.destroy()
        sys.exit()


if __name__ == "__main__":
    particles = create_particles(NUM_PARTICLES)
    game = Game(particles)
    game.show_controls()
    simulation_loop(game.update, TIMESTEP, particles)