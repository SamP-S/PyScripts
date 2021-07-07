import pygame
from random import randint, uniform
from circle import *
from numerical import *
import time
import math

# calls pygame module to create an instance of itself
pygame.init()

# create constant objects
WIDTH = 400
HEIGHT = 300
ASPECT = WIDTH/HEIGHT
DISPLAY = pygame.display
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN_RECT = pygame.Rect(0, 0, WIDTH, HEIGHT)
NUM_CIRCLES = 100
CIRCLE_MIN = 10
CIRCLE_MAX = 12
VEL_MIN = 50
VEL_MAX = 100
COLOURS = {
    "BLACK" : (0, 0, 0),
    "WHITE" : (255, 255, 255),
    "RED" : (255, 0, 0),
    "GREEN" : (0, 255, 0),
    "BLUE" : (0, 0, 255),
    "YELLOW" : (255, 255, 0),
    "CYAN" : (0, 255, 255),
    "MAGENTA" : (255, 0, 255)
}

def rand_circle():
    r = randint(CIRCLE_MIN, CIRCLE_MAX)
    x = randint(r, WIDTH - r)
    y = randint(r, HEIGHT - r)
    vx = randneg(uniform(VEL_MIN, VEL_MAX))
    vy = randneg(uniform(VEL_MIN, VEL_MAX))
    colour_index = randint(1, len(COLOURS) - 1)
    key = list(COLOURS.keys())[colour_index]
    return Circle(x, y, r, vx, vy, COLOURS[key])

world = []
for i in range(NUM_CIRCLES):
    world.append(rand_circle())

# # corners collide
# a = Circle(0, 0, 10, VEL_MIN * ASPECT, VEL_MIN, COLOURS["RED"])
# b = Circle(WIDTH, HEIGHT, 10, -VEL_MIN * ASPECT, -VEL_MIN, COLOURS["GREEN"])
# world.append(a)
# world.append(b)

# # billiard example
# a = Circle(20, 50, 20, 200, 0, COLOURS["GREEN"])
# b = Circle(100, 50, 20, 0, 0, COLOURS["RED"])
# c = Circle(140, 50, 20, 0, 0, COLOURS["RED"])
# d = Circle(180, 50, 20, 0, 0, COLOURS["RED"])
# e = Circle(220, 50, 20, 0, 0, COLOURS["RED"])
# f = Circle(260, 50, 20, 0, 0, COLOURS["RED"])
# g = Circle(300, 50, 20, 0, 0, COLOURS["YELLOW"])
# world.append(a)
# world.append(b)
# world.append(c)
# world.append(d)
# world.append(e)
# world.append(f)
# world.append(g)

print(type(SURFACE))
print(type(DISPLAY))

time_start = time.time()
time_frame = time.time()

# main loop
is_quit = False
while not is_quit:
    dt = (time.time() - time_frame)
    # print(dt)
    time_frame = time.time()
    
    # poll events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_quit = True
    total_mom = 0
    # move circles
    for obj in world:
        total_mom += math.sqrt(obj.vx * obj.vx + obj.vy * obj.vy) * obj.r
        obj.move(dt)
    # print("total mom in sys:", total_mom)

    # calculating physics
    for depth in range(5):
        for i in range(len(world)):
            for j in range(i + 1, len(world)):
                # stop collision with itself
                if i == j:
                    continue
                if check_circle_collision(world[i], world[j]):
                    handle_circle_collision(world[i], world[j])

    # window edge collision
    for obj in world:
        if obj.min_x() <= 0:
            obj.vx = positive(obj.vx)
        elif obj.max_x() >= WIDTH:
            obj.vx = negative(obj.vx)

        if obj.min_y() <= 0:
            obj.vy = positive(obj.vy)
        elif obj.max_y() >= HEIGHT:
            obj.vy = negative(obj.vy)
        
                

    # rendering
    pygame.draw.rect(SURFACE, COLOURS["BLACK"], SCREEN_RECT)
    for i in range(len(world)):
        pos = (world[i].x, world[i].y)
        pygame.draw.circle(SURFACE, world[i].colour, pos, world[i].r)
    pygame.display.flip()

# safely destroys pygame instance
pygame.quit()