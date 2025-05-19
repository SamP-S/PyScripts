from math import *
import pygame as pg
import numpy as np


def main():
    
    # initalise
    pg.init()
    WIDTH = 800
    HEIGHT = 600
    window = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Double Pendulum")
    clock = pg.time.Clock()

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
    ox = WIDTH // 2
    oy = 3 * HEIGHT // 4
    
    # pendulum dynamic parameters
    phi = 0
    d_phi = 2 * pi
    d2_phi = 0
    
    # # centre of mass arm 1
    # cm_x1 = 0.5 * l * sin(phi)
    # cm_y1 = -0.5 * l * cos(phi)

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
        phi += d_phi * dt
        x1 = ox + l * sin(phi)
        y1 = oy - l * cos(phi)
        
        # draw
        window.fill(COLOURS["background"])
        pg.draw.line(window, COLOURS["secondary"], (ox, oy), (x1, y1), LIMB_WIDTH)
        pg.draw.circle(window, COLOURS["primary"], (ox, oy), JOINT_RADIUS)
        pg.draw.circle(window, COLOURS["primary"], (x1, y1), JOINT_RADIUS)

        # swap display buffers
        pg.display.update()

    # cleanup resources
    pg.quit()

if __name__ == "__main__":
    main()