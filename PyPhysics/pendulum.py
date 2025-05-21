from math import *
import pygame as pg
import numpy as np
from copy import copy

# DRAWING
COLOURS = {
    "background": pg.Color(0, 0, 0),
    "primary": pg.Color(127, 255, 127),
    "secondary": pg.Color(255, 127, 127),
    "tertiary": pg.Color(127, 127, 255),
}
JOINT_RADIUS = 5
LIMB_WIDTH = 2
M_PIXEL_SCALE = 100    
# WINDOW
WIDTH = 800
HEIGHT = 600
# PHYSICS
G = 9.81

# pendulum
l = 1
m = 10
ox = 4
oy = 4
theta_0 = pi / 2

# formulas
# i = m * l**2              # moment of inertia
# tau = f * sin(theta) * l  # torque

def energy(tn):
    # energy
    kinetic = 0.5 * m * (tn[1] * l) ** 2
    potential = m * G * l * (1 - cos(tn[0]))
    total = kinetic + potential
    print(f"ke: {kinetic:.2f};\t pe: {potential:.2f};\t total: {total:.2f}")


def calc_step(dt, t0):
    d_theta = t0[1] + t0[2] * dt
    theta = t0[0] + d_theta * dt
    d2_theta = -G * sin(theta) 
    return (theta, d_theta, d2_theta)
    
def main():    
    # initalise
    pg.init()
    window = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Double Pendulum")
    clock = pg.time.Clock()
    
    t0 = (theta_0, 0.0, G * sin(theta_0))
    print("initial")
    energy(t0)
    
    # main loop
    print("loop")
    quit_flag = False
    while quit_flag == False:
        dt = clock.tick(60) / 1000
        
        # handle events
        for evt in pg.event.get():
            if evt.type == pg.QUIT:
                quit_flag = True

        # calculate
        tn = calc_step(dt, t0)
        energy(tn)
        
        # graphical coordinates
        gox = ox * M_PIXEL_SCALE
        goy = oy * M_PIXEL_SCALE
        x1 = (ox + l * sin(tn[0])) * M_PIXEL_SCALE
        y1 = (oy - l * cos(tn[0])) * M_PIXEL_SCALE
        
        # draw commands
        window.fill(COLOURS["background"])
        pg.draw.line(window, COLOURS["secondary"], (gox, goy), (x1, y1), LIMB_WIDTH)
        pg.draw.circle(window, COLOURS["primary"], (gox, goy), JOINT_RADIUS)
        pg.draw.circle(window, COLOURS["primary"], (x1, y1), JOINT_RADIUS)

        # swap display buffers
        pg.display.update()
        t0 = tn

    # cleanup resources
    pg.quit()

if __name__ == "__main__":
    main()