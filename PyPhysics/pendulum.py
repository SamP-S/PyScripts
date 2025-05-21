from math import *
import pygame as pg
import numpy as np

G = 9.81
COLOURS = {
    "background": pg.Color(0, 0, 0),
    "primary": pg.Color(127, 255, 127),
    "secondary": pg.Color(255, 127, 127),
    "tertiary": pg.Color(127, 127, 255),
}
JOINT_RADIUS = 5
LIMB_WIDTH = 2
M_PIXEL_SCALE = 100    
WIDTH = 800
HEIGHT = 600


class Pendulum:
    
    def __init__(self):
        # static
        self.l = 1
        self.m = 10
        self.ox = 4
        self.oy = 4
        
        # dynamic
        self.theta = pi / 2
        self.f = self.m * G * sin(self.theta)
        self.d_theta = 0.0
        self.d2_theta = 0.0
        
    def energy(self):
        # energy
        kinetic = 0.5 * self.m * (self.d_theta * l) ** 2
        potential = self.m * G * self.l * (1 - cos(self.theta))
        total = kinetic + potential
        print(f"ke: {kinetic};\t pe: {potential};\t total: {total}")


def func(dt, t0, tn):
    
    ## calculate
    # i = m * l**2            # moment of inertia
    # tau = f * sin(theta) * l  # torque
    
    f = tn.m * G               # total linear force
    f_perp = f * sin(theta)   # perpendicular
    f_para = f * cos(theta)   # parallel
    d2_theta = f_perp / m     # f = ma -> f/m = a
    


def main():    
    # initalise
    pg.init()
    window = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Double Pendulum")
    clock = pg.time.Clock()

    t = []
    t0 = Pendulum()
    t.append(t0)
    
    # main loop
    quit_flag = False
    while quit_flag == False:
        dt = clock.tick(60) / 1000
        print(pg.time.get_ticks() / 1000)
        
        # handle events
        for evt in pg.event.get():
            if evt.type == pg.QUIT:
                quit_flag = True

        # calculate
        tn = Pendulum()
        func(dt, t0, tn)
        
        # graphical coordinates
        x1 = (tn.ox + tn.l * sin(tn.theta)) * M_PIXEL_SCALE
        y1 = (tn.oy - tn.l * cos(tn.theta)) * M_PIXEL_SCALE
        
        # draw commands
        window.fill(COLOURS["background"])
        pg.draw.line(window, COLOURS["secondary"], (ox, oy), (x1, y1), LIMB_WIDTH)
        pg.draw.circle(window, COLOURS["primary"], (ox, oy), JOINT_RADIUS)
        pg.draw.circle(window, COLOURS["primary"], (x1, y1), JOINT_RADIUS)

        # swap display buffers
        pg.display.update()
        t0 = tn

    # cleanup resources
    pg.quit()

if __name__ == "__main__":
    main()