# external modules
import pygame
from pygame.locals import *

from vectors import *
import dist

HEIGHT = 480
WIDTH = 480

# line class for storing pygame lines for constant/repeated use
class line:
    # init takes required pygame line arguements
    def __init__(self, colour, start, end, thickness=1):
        self.colour = colour
        self.start = start
        self.end = end
        self.thickness = thickness
    # draw function requires a surface to draw on
    def draw(self, surface):
        pygame.draw.line(surface, self.colour, self.start, self.end, self.thickness)

# rectangle class for storing pygame rect for constant/repeated use
class rect:
    # init takes required pygame rect arguements
    def __init__(self, colour, position, size, thickness=0):
        self.colour = colour
        self.position = position
        self.size = size
        self.thickness = thickness
    # draw function requires a surface to draw on
    def draw(self, surface):
        r = [ self.position.x, self.position.y,
              self.size.x, self.size.y ]
        pygame.draw.rect(surface, self.colour, r, self.thickness)

# box class with centre and size
class box:
    def __init__(self, colour, centre, size, thickness=0):
        self.colour = colour
        self.centre = centre
        self.size = size
        self.thickness = thickness
    def draw(self, surface):
        r = [   self.centre.x - self.size.x, 
                self.centre.y - self.size.y,
                self.size.x * 2,
                self.size.y * 2
        ]
        pygame.draw.rect(surface, self.colour, r, self.thickness)

# circle class for storing pygame circle for constant/repeated use
class circle:
    # init takes required pygame circle arguements
    def __init__(self, colour, centre, radius, thickness=0):
        self.colour = colour
        self.centre = centre
        self.radius = radius
        self.thickness = thickness
    # draw function requires a surface to draw on
    def draw(self, surface):
        pygame.draw.circle(surface, self.colour, self.centre.arr, self.radius, self.thickness)


def main():
    pygame.init()

    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game")

    fore_col = pygame.Color(255, 0, 0)
    wall_col = pygame.Color(127, 127, 127)
    back_col = pygame.Color(0, 0, 0)

    mouse_pos = vec2()

    walls = []
    walls.append(box(wall_col, vec2(100, 200), vec2(50, 50)))
    walls.append(box(wall_col, vec2(300, 100), vec2(50, 100)))
    balls = []
    balls.append(circle(wall_col, vec2(250, 400), 75))

    while True:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                break
            if evt.type == pygame.MOUSEBUTTONDOWN:
                pass
            if evt.type == pygame.MOUSEBUTTONUP:
                pass
            if evt.type == pygame.MOUSEMOTION:
                mouse_pos.x = evt.pos[0]
                mouse_pos.y = evt.pos[1]

        radius = 2048
        display.fill(back_col)
        for w in walls:
            r = dist.signedDistToBox(mouse_pos, w.centre, w.size)
            if radius > r:
                radius = r
            w.draw(display)
        for b in balls:
            r = dist.signedDistToCircle(mouse_pos, b.centre, b.radius)
            if radius > r:
                radius = r
            b.draw(display)

        radius = int(radius)
        if radius < 0:
            radius = -radius
        circle(fore_col, mouse_pos, int(radius)).draw(display)

        # update display buffer
        pygame.display.update()
        #pygame.time.wait(100)


if __name__ == "__main__":
    main()