# dependancy modules
import pygame
from pygame.locals import *
# standard modules
import timer
import math

# WINDOW SETTINGS
WIDTH = 720
HEIGHT = 480
PIXEL_SCALE = 200
# DISPLAY SETTINGS
BACKGROUND_COLOUR = pygame.Color(0, 0, 0)
LINES_MAX = 1
# LINE CONSTANTS
LINE_COLOUR = pygame.Color(100, 100, 255)
LINE_LEN = math.sqrt(WIDTH * HEIGHT)
LINE_SIZE = 2
# WAVE CONSTANTS
WAVE_RES = 200
WAVE_FREQUENCY = 2
WAVE_AMPLITUDE = 1
WAVE_SPEED = 1
WAVE_COLOUR = pygame.Color(255, 255, 255)

# window coordinate system class
# put in window size and pixel scale
# to get easy coordinate system mapping
class window:
    def __init__(self, width, height, pixel_scale):
        self.width = width
        self.height = height
        self.pixel_scale = pixel_scale

    def get_window_width(self):
        return self.width
    def get_window_height(self):
        return self.height
    def get_pixel_scale(self):
        return self.pixel_scale
    def set_pixel_scale(self, scl):
        self.pixel_scale = scl
    def get_graph_width(self):
        return self.width / self.pixel_scale
    def get_graph_height(self):
        return self.height / self.pixel_scale

    def window_to_graph(self, coord):
        return (
            (coord[0] - self.width / 2) / self.pixel_scale,     # x
            (coord[1] - self.height / 2) / self.pixel_scale     # y
        )
    def graph_to_window(self, coord):
        return (    
            coord[0] * self.pixel_scale + self.width / 2,       # x
            coord[1] * self.pixel_scale + self.height / 2       # y
        )

coord_sys = window(WIDTH, HEIGHT, PIXEL_SCALE)

# line class for storing pygame lines for constant/repeated use
class line:
    # init takes required arguements
    def __init__(self, colour, start, end, size=1):
        self.colour = colour
        self.start = start
        self.end = end
        self.size = size
    # draw function requires a surface to draw on
    def draw(self, surface):
        pygame.draw.line(surface, self.colour, self.start, self.end, self.size)

# y = m * x + c
# linear equation class for graph drawing
class linear_line:
    # takes colour, gradient, y-offset, thickness
    def __init__(self, colour, m, c, size=1):
        self.colour = colour
        self.m = m
        self.c = c
        self.size = size
    # draw call requires pygame surface to draw on
    # and requires coordinate system class for mapping graph to window
    def draw(self, surface, coord_system):
        # min & max -> x-axis
        min_x = -coord_system.get_graph_width() / 2
        max_x = -min_x
        # start and end points
        start_graph = (min_x, min_x * self.m + self.c)
        end_graph = (max_x, max_x * self.m + self.c)
        start = coord_system.graph_to_window(start_graph)
        end = coord_system.graph_to_window(end_graph)
        # pygame draw call
        pygame.draw.line(surface, self.colour, start, end, self.size)

# sine wave class for drawing sine wave
class sine:
    def __init__(self, colour, frequency, amplitude):
        self.colour = colour
        self.freq = frequency
        self.amp = amplitude

    def draw(self, surface, offset, coord_system):
        min_x = -coord_system.get_graph_width() / 2
        delta_x = 2 * math.pi / WAVE_RES

        pxl = coord_system.get_pixel_scale()
        centre_x = coord_system.get_window_width() / 2
        centre_y = coord_system.get_window_height() / 2

        while  min_x < coord_system.get_graph_width() / 2:
            start = (
                centre_x + pxl * (min_x), 
                centre_y + pxl * (math.sin(min_x * self.freq + offset) * self.amp)
            )
            min_x += delta_x
            end = (
                centre_x + pxl * (min_x), 
                centre_y + pxl * (math.sin((min_x) * self.freq + offset) * self.amp)
            )
            pygame.draw.aaline(surface, self.colour, start, end)

# pygame initialisation
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

# constant variables
show_axis = False
tmr = timer.timer()
wave = sine(WAVE_COLOUR, WAVE_FREQUENCY, WAVE_AMPLITUDE)
lines = []

# axis line setup
start = (0, HEIGHT / 2)
end = (WIDTH, HEIGHT / 2)
axis_x = line((255, 0, 0), start, end, 1)
start = (WIDTH / 2, 0)
end = (WIDTH / 2, HEIGHT)
axis_y = line((0, 255, 0), start, end, 1)

# main loop
while True:
    # checks for quit
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            # exits
            pygame.quit()
            break
    
    # get time ellapsed since last frame
    delta_time = tmr.get_time(False)
    # y offset by trig function
    c_sin = math.sin(delta_time) * WAVE_AMPLITUDE
    c_cos = math.cos(delta_time) * WAVE_AMPLITUDE
    c_tan = math.tan(delta_time) * WAVE_AMPLITUDE
    # gradient by trig function
    m_sin = math.sin(delta_time) * WAVE_AMPLITUDE * WAVE_FREQUENCY
    m_cos = math.cos(delta_time) * WAVE_AMPLITUDE * WAVE_FREQUENCY
    m_tan = math.tan(delta_time) * WAVE_AMPLITUDE * WAVE_FREQUENCY

    # makes linear line and adds to list
    lines.append(linear_line(LINE_COLOUR, m_cos, c_sin, LINE_SIZE))
    # removes excess lines from list
    if len(lines) > LINES_MAX:
        lines.pop(0)
    
    # draw calls
    display.fill(BACKGROUND_COLOUR)
    if show_axis:
        axis_x.draw(display)
        axis_y.draw(display)
    wave.draw(display, delta_time, coord_sys)
    for l in lines:
        l.draw(display, coord_sys)
    # update display buffer
    pygame.display.update()