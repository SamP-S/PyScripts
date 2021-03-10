# collision detection for spheres or quick light detection
# much quicker as only a distance/radius is required
# then 3d pythagoras can be used
import math

# 3d vector for position and direction
class vec3:

    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

def v3_normalise(a):
    l = a.x * a.x + a.y * a.y + a.z * a.z
    r = math.sqrt(l)
    return vec3(a.x / r, a.y / r, a.z / r)


class sphere_collider:

    def __init__(self, pos, radius):
        self.pos = pos
        self.radius = radius
    
def check_collision(a, b):
    x = b.pos.x - a.pos.x
    y = b.pos.y - a.pos.y
    z = b.pos.z - a.pos.z
    dist = math.sqrt(x*x + y*y + z*z)
    if dist <= a.radius + b.radius:
        return True
    return False


def main():
    a = sphere_collider(vec3(0, 0, 0), 1)
    b = sphere_collider(vec3(1, 1, 1), 0.5)
    print(check_collision(a, b))

if __name__ == "__main__":
    main()