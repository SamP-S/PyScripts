from simulator import Simulator as Sim
from random import randint, uniform
from circle import *
from numerical import *
import time
import math


class Rigid_Physics_Simulation:
    NUM_CIRCLES = 100
    CIRCLE_MIN = 10
    CIRCLE_MAX = 12
    VEL_MIN = 50
    VEL_MAX = 100

    def rand_circle(self):
        r = randint(self.CIRCLE_MIN, self.CIRCLE_MAX)
        x = randint(r, Sim.WIDTH - r)
        y = randint(r, Sim.HEIGHT - r)
        vx = randneg(uniform(self.VEL_MIN, self.VEL_MAX))
        vy = randneg(uniform(self.VEL_MIN, self.VEL_MAX))
        colour_index = randint(1, len(Sim.COLOURS) - 1)
        key = list(Sim.COLOURS.keys())[colour_index]
        return Circle(x, y, r, vx, vy, Sim.COLOURS[key])

    def scenario_corners(self):
        # corners collide
        a = Circle(0, 0, 10, Sim.VEL_MIN * Sim.ASPECT, self.VEL_MIN, Sim.COLOURS["RED"])
        b = Circle(Sim.WIDTH, Sim.HEIGHT, 10, -self.VEL_MIN * Sim.ASPECT, -self.VEL_MIN, Sim.COLOURS["GREEN"])
        self.world.append(a)
        self.world.append(b)

    def scenario_billiard(self):
        # billiard example
        # set parameters
        vel, r, y, n = 200, 15, Sim.HEIGHT / 2, 5
        # add start ball with velocity
        circle_start = Circle(r, y, r, vel, 0, Sim.COLOURS["GREEN"])
        self.world.append(circle_start)
        # generate ball sequence
        for i in range(n):
            col = Sim.COLOURS["RED"]
            if i == n - 1:
                col = Sim.COLOURS["YELLOW"]
            c = Circle(100 + 2 * r * i, y, r, 0, 0, col)
            self.world.append(c)

    def scenario_particles(self):
        for i in range(self.NUM_CIRCLES):
            self.world.append(self.rand_circle())

    def __init__(self):
        self.world = []
        self.scenario_billiard()

    def update(self, dt):
        # move circles
        for obj in self.world:
            obj.move(dt)

        # calculating physics
        for depth in range(5):
            for i in range(len(self.world)):
                for j in range(i + 1, len(self.world)):
                    # stop collision with itself
                    if i == j:
                        continue
                    if check_circle_collision(self.world[i], self.world[j]):
                        handle_circle_collision(self.world[i], self.world[j])

        # window edge collision
        for obj in self.world:
            if obj.min_x() <= 0:
                obj.vx = positive(obj.vx)
            elif obj.max_x() >= Sim.WIDTH:
                obj.vx = negative(obj.vx)

            if obj.min_y() <= 0:
                obj.vy = positive(obj.vy)
            elif obj.max_y() >= Sim.HEIGHT:
                obj.vy = negative(obj.vy)

        # rendering
        Sim.DRAW.rect(Sim.SURFACE, Sim.COLOURS["BLACK"], Sim.SCREEN_RECT)
        for obj in self.world:
            pos = (obj.x, obj.y)
            Sim.DRAW.circle(Sim.SURFACE, obj.colour, pos, obj.r)
        Sim.DISPLAY.flip()

if __name__ == "__main__":
    rgs = Rigid_Physics_Simulation()
    sim = Sim(rgs)
    sim.main()