import pygame
from pygame.locals import *

from OpenGL.GLU import *
from OpenGL.GL import *

import math

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 360

cubeVertices = ((-1, -1, -1), (-1, -1, 1), (1, -1, 1), (1, -1, -1), (-1, 1, -1), (-1, 1, 1), (1, 1, 1), (1, 1, -1))
cubeQuads = ((0, 1, 2, 3), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0), (4, 7, 6, 5))
cubeEdges = ((0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7))
cubePoints = (0, 1, 2, 3, 4, 5, 6, 7)

# vec3 for position and direction
class vec3:

    def __init__(self, x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

def v3_normalise(a):
    l = a.x * a.x + a.y * a.y + a.z * a.z
    r = math.sqrt(l)
    return vec3(a.x / r, a.y / r, a.z / r)

class box:

    def __init__(self, pos, rot, scl):
        self.pos = pos
        self.rot = rot
        self.scl = scl

    def get_points(self):
        points = []
        for z_angle in range(-45, 46, 90):
            for y_angle in range(-45, 46, 90):
                for x_angle in range(-45, 46, 90):
                    x = math.sin(math.radians(x_angle + self.rot.y + self.rot.z)) * math.sqrt(2) * self.scl.x / 2 + self.pos.x
                    y = math.sin(math.radians(y_angle + self.rot.x + self.rot.z)) * math.sqrt(2) * self.scl.y / 2 + self.pos.y
                    z = math.sin(math.radians(z_angle + self.rot.x + self.rot.y)) * math.sqrt(2) * self.scl.z / 2 + self.pos.z
                    print("x:", x, " y:", y, " z:", z)
                    point = vec3(x,y,z)
                    points.append(point)
        return points

# definitions
def glWindow():
    pygame.init()
    window = pygame.display
    #pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), DOUBLEBUF|OPENGL)
    pygame.display.set_caption("bruh")
    gluPerspective(45, WINDOW_WIDTH/WINDOW_HEIGHT, 0.1, 50)
    glTranslatef(0, 0, -5)
    glScalef(0.5, 0.5, 0.5)


def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


def quadCube():
    glBegin(GL_QUADS)
    for cubeQuad in cubeQuads:
        for cubeVertex in cubeQuad:
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()


def edgeCube():
    glBegin(GL_LINES)
    for cubeEdge in cubeEdges:
        for cubeVertex in cubeEdge:
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()


def pointCube():
    glBegin(GL_POINTS)
    for cubeVertex in cubePoints:
        glVertex3fv(cubeVertices[cubeVertex])
    glEnd()


def main():
    print("pyopengl")
    glWindow()
    frame = 0
    while True:
        handleEvents()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glRotatef(0.5, 1, 1.5, 1)
        cube_type = (frame // 60) % 3
        if cube_type == 0:
            quadCube()
        elif cube_type == 1:
            edgeCube()
        else:
            pointCube()
        pygame.display.flip()
        pygame.time.wait(10)
        frame += 1


if __name__ == "__main__":
    main()
