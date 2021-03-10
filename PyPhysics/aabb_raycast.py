# AABB raycasting collision detection
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

# position is central to the box not bottom, close, left
class box_collider:

    def __init__(self, x,y,z,w,h,d):
        self.x = x
        self.y = y
        self.z = z
        self.width = w
        self.height = h
        self.depth = d
    
    

class ray:

    def __init__(self, pos, dir, len):
        self.pos = pos
        self.dir = v3_normalise(dir)
        self.len = len

    def SetDirection(self, x, y, z):
        self.dir = v3_normalise(vec3(x,y,z))


def check_collision(box, ray):
    left = box.x - box.width/2
    right = left + box.width
    bottom = box.y - box.height/2
    top = box.y + box.height
    front = box.z - box.depth/2
    back = box.z + box.depth

    x_min = x_max = y_min = y_max = z_min = z_max = False

    dist = (left - ray.pos.x) / ray.dir.x
    if dist <= ray.len:
        if ray.pos.y + ray.dir.y * dist >= bottom and ray.pos.y + ray.dir.y * dist <= top:
            if ray.pos.z + ray.dir.z * dist >= front and ray.pos.z + ray.dir.z * dist <= back:
                x_min = True
    
    dist = (right - ray.pos.x) / ray.dir.x
    if dist <= ray.len:
        if ray.pos.y + ray.dir.y * dist >= bottom and ray.pos.y + ray.dir.y * dist <= top:
            if ray.pos.z + ray.dir.z * dist >= front and ray.pos.z + ray.dir.z * dist <= back:
                x_max = True

    dist = (bottom - ray.pos.y) / ray.dir.y
    if dist <= ray.len:
        if ray.pos.x + ray.dir.x * dist >= left and ray.pos.x + ray.dir.x * dist <= right:
            if ray.pos.z + ray.dir.z * dist >= front and ray.pos.z + ray.dir.z * dist <= back:
                y_min = True

    dist = (top - ray.pos.y) / ray.dir.y
    if dist <= ray.len:
        if ray.pos.x + ray.dir.x * dist >= left and ray.pos.x + ray.dir.x * dist <= right:
            if ray.pos.z + ray.dir.z * dist >= front and ray.pos.z + ray.dir.z * dist <= back:
                y_max = True

    dist = (front - ray.pos.z) / ray.dir.z
    if dist <= ray.len:
        if ray.pos.x + ray.dir.x * dist >= left and ray.pos.x + ray.dir.x * dist <= right:
            if ray.pos.y + ray.dir.y * dist >= bottom and ray.pos.y + ray.dir.y * dist <= top:
                z_min = True

    dist = (back - ray.pos.z) / ray.dir.z
    if dist <= ray.len:
        if ray.pos.x + ray.dir.x * dist >= left and ray.pos.x + ray.dir.x * dist <= right:
            if ray.pos.y + ray.dir.y * dist >= bottom and ray.pos.y + ray.dir.y * dist <= top:
                z_max = True

    print("x_min: ", x_min)
    print("x_max: ", x_max)
    print("y_min: ", y_min)
    print("y_max: ", y_max)
    print("z_min: ", z_min)
    print("z_max: ", z_max)
    return x_min or x_max or y_min or y_max or z_min or z_max


def main():
    r = ray(vec3(-1, -1, -1), vec3(1, 1, 1), 0.87)
    b = box_collider(0, 0, 0, 1, 1, 1)
    print(check_collision(b, r))

if __name__ == "__main__":
    main()