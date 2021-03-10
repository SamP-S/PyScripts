# external modules
import pygame
from pygame.locals import *

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
        r = [ self.position[0], self.position[1],
              self.size[0], self.size[1] ]
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
        pygame.draw.circle(surface, self.colour, self.centre, self.radius, self.thickness)


def main():
    pygame.init()

    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game")
    
    cursor = circle(pygame.Color(255, 255, 255), (0, 0), 10)

    background_colour = pygame.Color(0, 0, 0)
    axis_x_colour = pygame.Color(255, 0, 0, 255)
    axis_y_colour = pygame.Color(0, 255, 0, 255)

    axis_size = 1
    lines = []
    layers_max = 2000

    while True:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                break
            if evt.type == pygame.MOUSEBUTTONDOWN:
                cursor.radius += 10
            if evt.type == pygame.MOUSEBUTTONUP:
                cursor.radius -= 10
            if evt.type == pygame.MOUSEMOTION:
                cursor.centre = (evt.pos[0], evt.pos[1])
        
        lines.append(line(axis_x_colour, (cursor.centre[0], 0), (cursor.centre[0], HEIGHT), axis_size))
        lines.append(line(axis_y_colour, (0, cursor.centre[1]), (WIDTH, cursor.centre[1]), axis_size))

        # remove axis
        if len(lines) > layers_max:
            lines.pop(0)
            lines.pop(0)

        # draw directly on display
        display.fill(background_colour)
        cursor.draw(display)
        for axis in lines:
            axis.draw(display)

        # update display buffer
        pygame.display.update()


if __name__ == "__main__":
    main()