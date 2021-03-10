import random as r
import pygame
from pygame.locals import *
from pygame import gfxdraw


# constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
NUM_NODES = 10
NODE_RADIUS = 10
FONT_SIZE = 12
LINE_WIDTH = 2

# colours
COLOUR_WHITE = (255, 255, 255)
COLOUR_BLACK = (0, 0, 0)
COLOUR_RED = (255, 0, 0)
COLOUR_GREEN = (0, 255, 0)
COLOUR_BLUE = (0, 0, 255)
COLOUR_YELLOW = (255, 255, 0)
COLOUR_CYAN = (0, 255, 255)
COLOUR_MAGENTA = (255, 0, 255)


# classes
class edge:

    def __init__(self, a, b, weight = -1):
        self.nodes = [a, b]
        self.weight = weight

    def draw(self):
        g = pygame.display.get_surface()
        start = (self.nodes[0].x, self.nodes[0].y)
        end = (self.nodes[1].x, self.nodes[1].y)
        pygame.draw.line(g, COLOUR_WHITE, start, end, LINE_WIDTH)


class node:
    
    def __init__(self, x, y, i):
        #print(x, ", ", y)
        self.x = x
        self.y = y
        self.id = i
        self.connected = []


    def connect(self, b):
        self.connected.append(edge(self, b))


    def print_node(self):
        print("x: ", self.x, ", y: ", self.y)
        for edge in self.connected:
            print("edge: ", edge)


    def draw(self):
        g = pygame.display.get_surface()
        font = pygame.font.SysFont("Terminus", FONT_SIZE)
        text = font.render(str(self.id), True, COLOUR_BLACK)
        textRect = text.get_rect()
        textRect.center = (self.x, self.y)
        pygame.draw.circle(g, COLOUR_WHITE, [self.x, self.y], NODE_RADIUS)
        #pygame.gfxdraw.aacircle(g, self.x, self.y, NODE_RADIUS, COLOUR_WHITE)
        g.blit(text, textRect)
        for line in self.connected:
            line.draw()


# definitons
def init():
    pygame.init()
    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("node graphs")
    #pygame.font.Font("Terminus", 9)

def handleEvents():
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        pygame.quit()
        quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


# main loop
def main():
    print("node graphs")
    init()
    nodes = [node(-1, -1, -1) for i in range(NUM_NODES)]
    for i in range(NUM_NODES):
        x = r.randint(0, WINDOW_WIDTH)
        y = r.randint(0, WINDOW_HEIGHT)
        nodes[i] = node(x, y, i)
    
    no_edges = (int)((float)(NUM_NODES) * (r.random() + 1))
    for i in range(no_edges):
        a = r.randint(0, NUM_NODES - 1)
        b = r.randint(0, NUM_NODES - 1)
        nodes[a].connect(nodes[b])
        nodes[b].connect(nodes[a])

    while True:
        handleEvents()
        for point in nodes:
            point.draw()
        pygame.display.flip()
        pygame.time.wait(10)


# calls main if NOT an import
if __name__ == "__main__":
    main()
