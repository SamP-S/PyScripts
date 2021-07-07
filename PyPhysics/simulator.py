import pygame
import time

class Simulator:

    # create constant objects
    WIDTH = 400
    HEIGHT = 300
    ASPECT = WIDTH/HEIGHT
    DISPLAY = pygame.display
    SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
    DRAW = pygame.draw
    SCREEN_RECT = pygame.Rect(0, 0, WIDTH, HEIGHT)
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

    def __init__(self, _simulation):
        print(type(self.SURFACE))
        print(type(self.DISPLAY))    

        # calls pygame module to create an instance of itself
        pygame.init()
        self.simulation = _simulation
        self.world = []
        self.time_start = time.time()
        self.time_frame = self.time_start

    def main(self):
        # main loop
        is_quit = False
        while not is_quit:
            dt = (time.time() - self.time_frame)
            self.time_frame = time.time()
            
            # poll events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_quit = True
            
            self.simulation.update(dt)

        # safely destroys pygame instance
        pygame.quit()