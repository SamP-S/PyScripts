from math import *
import pygame as pg
import numpy as np


def main():
    
    # initalise
    pg.init()
    window = pg.display.set_mode((800, 600))
    pg.display.set_caption("Double Pendulum")

    COLOURS = {
        "background": pg.Color(0, 0, 0),
        "primary": pg.Color(127, 255, 127),
        "secondary": pg.Color(255, 127, 127),
        "tertiary": pg.Color(127, 127, 255),
    }
    JOINT_RADIUS = 5
    LIMB_WIDTH = 2
    
    # pendulum static parameters
    l = 100
    m = 10
    g = 9.81
    ox = 100
    oy = 100
    
    # pendulum dynamic parameters
    phi = pi / 4
    d_phi = 0
    d2_phi = 0
    
    # # centre of mass arm 1
    # cm_x1 = 0.5 * l * sin(phi)
    # cm_y1 = -0.5 * l * cos(phi)

    while True:
        for evt in pg.event.get():
            if evt.type == pg.QUIT:
                break

        # calculate
        x1 = ox + l * sin(phi)
        y1 = oy - l * cos(phi)
        
        # draw
        window.fill(COLOURS["background"])
        pg.draw.circle(window, COLOURS["primary"], (ox, oy), JOINT_RADIUS)
        pg.draw.line(window, (ox, oy), (x1, y1), COLOURS["secondary"], LIMB_WIDTH)
        pg.draw.circle(window, COLOURS["primary"], (x1, y1), JOINT_RADIUS)

        # swap display buffers
        pg.display.update()

    # cleanup resources
    pg.quit()

if __name__ == "__main__":
    main()