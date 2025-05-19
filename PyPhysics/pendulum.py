from math import *
import pygame as pg
import numpy as np


def main():
    
    # initalise
    pg.init()
    window = pg.display.set_mode((800, 600))
    pg.display.set_caption("Double Pendulum")

    colours = {
        "bg": pg.Color(0, 0, 0),
        "line": pg.Color(127, 255, 127),
        "joint": pg.Color(255, 127, 127),
    }
    
    l1 = 100
    ox = 0
    oy = 0
    phi = pi / 4
    d_phi = 0
    d2_phi = 0
    
    # centre of mass arm 1
    cm_x1 = 0.5 * l1 * sin(phi)
    cm_y1 = -0.5 * l1 * cos(phi)

    # langarian
    

    while True:
        for evt in pg.event.get():
            if evt.type == pg.QUIT:
                break

        window.fill(colours["bg"])
    

        # swap display buffers
        pg.display.update()

    # cleanup resources
    pg.quit()

if __name__ == "__main__":
    main()