from math import *
import pygame as pg
import numpy as np
from copy import copy
import matplotlib.pyplot as plt

# double pendulum
# mass is at the end of the each limb
ox = 4
oy = 4
l0 = 1
l1 = 1  
m0 = 1
m1 = 1
init_theta_0 = pi / 2
init_theta_1 = pi / 4

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
G = 10
STEPS_PER_SECOND = 500
TIMESTEPS = STEPS_PER_SECOND * 5


def energy(tn):
    # calculate cartesian coordinates
    x0 = l0 * sin(tn[0][0])
    y0 = - l0 * cos(tn[0][0])
    x1 = x0 + l1 * sin(tn[1][0])
    y1 = y0 - l1 * cos(tn[1][0])
    
    # energy
    kinetic = 0.5 * m * (tn[1] * l) ** 2
    potential = -G * (m0 * y0 + m1 * y1)
    total = kinetic + potential
    # print(f"ke: {kinetic:.2f};\t pe: {potential:.2f};\t total: {total:.2f}")
    return (kinetic, potential, total)

def calc_step(dt, t0):
    d_theta = t0[1] + t0[2] * dt
    theta = t0[0] + d_theta * dt
    d2_theta = -G * sin(theta) / l
    # print(f"theta: {theta:.2f};\t d theta: {d_theta:.2f};\t d2 theta: {d2_theta:.2f}")
    return (theta, d_theta, d2_theta)

def sim():
    print("pendulum sim")
    dt = 1 / STEPS_PER_SECOND
    t = np.zeros((TIMESTEPS, 3))
    e = np.zeros((TIMESTEPS, 3))
    x = np.arange(0.0, TIMESTEPS * dt, dt)
    
    # set first step
    t[0][0] = init_theta_0
    t[0][1] = 0.0
    t[0][2] = -G * sin(init_theta_0) / l
        
    # calculate sequentially
    for i in range(1, TIMESTEPS):
        t[i] = calc_step(dt, t[i-1])
    
    # calculte energy at each time step
    e = np.apply_along_axis(lambda tn: energy(tn), axis=1, arr=t)
    return t, e, x
    
    
def main():    
    # run pendulum simulation
    t, e, x = sim()

    # visualise
    if False:
        pg.init()
        window = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Single Pendulum")
        clock = pg.time.Clock()
        
        # main loop
        print("loop")
        quit_flag = False
        for i in range(len(x)):
            dt = clock.tick(STEPS_PER_SECOND) / 1000
            
            # handle events
            for evt in pg.event.get():
                if evt.type == pg.QUIT:
                    break
            
            # graphical coordinates
            gox = ox * M_PIXEL_SCALE
            goy = HEIGHT - oy * M_PIXEL_SCALE
            x1 = (ox + l * sin(t[i][0])) * M_PIXEL_SCALE
            y1 = HEIGHT - (oy - l * cos(t[i][0])) * M_PIXEL_SCALE
            
            # draw commands
            window.fill(COLOURS["background"])
            pg.draw.line(window, COLOURS["secondary"], (gox, goy), (x1, y1), LIMB_WIDTH)
            pg.draw.circle(window, COLOURS["primary"], (gox, goy), JOINT_RADIUS)
            pg.draw.circle(window, COLOURS["primary"], (x1, y1), JOINT_RADIUS)

            # swap display buffers
            pg.display.update()

        # cleanup resources
        pg.quit()
    
    def print_stats(name, series):
        print(f"{name}: min={np.min(series):.3f};\t avg={np.mean(series):.5f};\t max={np.max(series):.3f}")
    
    # numpy the data
    theta, d_theta, d2_theta = np.array(t).T
    ke, pe, te = np.array(e).T
    print_stats("ke", ke)
    print_stats("pe", pe)
    print_stats("te", te)
    
    # energy graph
    # plt.plot(x, ke, label="Kinetic Energy")
    # plt.plot(x, pe, label="Potential Energy")
    # plt.plot(x, te, label="Total Energy")
    # plt.xlabel("Time (s)")
    # plt.ylabel("Energy (j)")
    # plt.title("Pendulum Energy")
    # plt.legend()
    # plt.show()
    
    # angular graph
    # plt.plot(x, theta, label="Theta")
    # plt.plot(x, d_theta, label="d Theta")
    # plt.plot(x, d2_theta, label="d2 Theta")
    # plt.xlabel("Time (s)")
    # plt.ylabel("Value")
    # plt.title("Pendulum Angular")
    # plt.legend()
    # plt.show()
    
    # # combined graph
    # fig, ax1 = plt.subplots()
    # ax1.set_xlabel("Time (s)")
    # ax1.set_ylabel("Energy (j)")
    # ax1.plot(x, ke, label="Kinetic Energy", linestyle="--")
    # ax1.plot(x, pe, label="Potential Energy", linestyle="--")
    # ax1.plot(x, te, label="Total Energy", linestyle="--")
    # ax1.tick_params(axis="y")
    # ax1.legend(loc="upper left")
    # ax2 = ax1.twinx()
    # ax2.set_ylabel("Angular Values")
    # ax2.plot(x, theta, label="Theta")
    # ax2.plot(x, d_theta, label="d Theta")
    # ax2.plot(x, d2_theta, label="d2 Theta")
    # ax2.tick_params(axis="y")
    # ax2.legend(loc="upper right")
    # plt.title("Combined Pendulum Graph")
    # fig.tight_layout()
    # plt.show()
    

if __name__ == "__main__":
    main()