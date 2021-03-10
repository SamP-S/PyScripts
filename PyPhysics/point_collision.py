# detecting a single point inside of a box
# the box has position, rotation and scale

import math

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

# box collider
class box_collider:

    def __init__(self, pos, rot, scl):
        self.pos = pos
        self.rot = rot
        self.scl = scl

    # needs rotation added

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

# need cube points to then generate planes to project point onto to figure out if ellapsing

# collision detection
def check_collision(p, box):
    None

def main():
    p = vec3()
    box = box_collider(vec3(0.5, 0.5, 0.5), vec3(45, 0, 0), vec3(1, 1, 1))
    points = box.get_points()
    print(check_collision(p, box))

if __name__ == "__main__":
    main()