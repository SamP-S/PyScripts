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
    x1 = 0
    y1 = 0
    theta1 = pi / 4
    theta1_v = 0
    theta1_a = 0
    
    l2 = 100
    theta2 = pi / 2
    theta2_v = 0
    theta2_a = 0
    
    # centre of mass arm 1
    x1 = 0.5 * l1 * sin(theta1)
    y1 = -0.5 * l1 * cos(theta1)
    # centre of mass arm 2
    x2 = l1 * sin(theta1) + 0.5 * l2 * sin(theta2)
    y2 = -l1 * cos(theta1) + -0.5 * l2 * cos(theta2)

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