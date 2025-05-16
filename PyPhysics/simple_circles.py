import pygame as pg
import random as R

# DEFINITIONS
class Circle:
    
    def __init__(self, r=10, pos=(150, 150), vel=(0, 0), colour=(255, 255, 255)):
        self.r = r
        self.pos = pos
        self.vel = vel
        self.colour = colour
        


# CONSTANTS
BG_COLOR = (20, 20, 20)
MAX_CIRCLES = 10
MAX_RADIUS = 10
MAX_VELOCITY = 5
FPS = 60.0

# INITIALISATION    
pg.init()
bounds = (0, 300, 0, 300)
screen = pg.display.set_mode((bounds[1], bounds[3]))
clock = pg.time.Clock()
pg.display.set_caption(("Greer"))

def gen_rand_circle():
    rad = R.randint(1, MAX_RADIUS)
    x = R.randint(0, bounds[1])
    y = R.randint(0, bounds[3])
    vx = R.randint(-MAX_VELOCITY, MAX_VELOCITY)
    vy = R.randint(-MAX_VELOCITY, MAX_VELOCITY)
    r = R.randint(0, 255)
    g = R.randint(0, 255)
    b = R.randint(0, 255)
    return Circle(r=rad, pos=(x, y), vel=(vx, vy), colour=(r, g, b))
circles = [gen_rand_circle() for i in range(MAX_CIRCLES)]

# MAIN LOOP
isQuit = False
while not isQuit:
    # GET DELTA TIME
    delta = clock.tick(FPS)
    
    # EVENT HANDLING
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isQuit = True
        elif event.type == pg.WINDOWRESIZED:
            w, h = pg.display.get_window_size()
            bounds = (0, w, 0, h)

    screen.fill(BG_COLOR)
    
    for c in circles:
        pg.draw.circle(surface=screen, color=c.colour, center=c.pos, radius=c.r)
    pg.display.flip()
    