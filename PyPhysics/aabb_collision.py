# axis aligned - boundary box collision detection (AABB)
# collision boxes are all parallel/perpendicular to x,y & z axis
# simplest form of collision detection

class vec3:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z


# position is central to the box not bottom, close, left
class box_collider:

    def __init__(self, x,y,z,w,h,d):
        self.x = x
        self.y = y
        self.z = z
        self.width = w
        self.height = h
        self.depth = d


def check_collision(a,b):
    x_min = x_max = False
    y_min = y_max = False
    z_min = z_max = False
        
    # x-axis
    if a.x - a.width/2 >=  b.x - b.width/2 and a.x - a.width/2 <= b.x + b.width/2:
        x_min = True
    if a.x + a.width/2 >=  b.x - b.width/2 and a.x - a.width/2 <= b.x + b.width/2:
        x_max = True

    # y-axis
    if a.y - a.height/2 >=  b.y - b.height/2 and a.y - a.height/2 <= b.y + b.height/2:
        y_min = True
    if a.y + a.height/2 >=  b.y - b.height/2 and a.y - a.height/2 <= b.y + b.height/2:
        y_max = True

    # z-axis
    if a.z - a.depth/2 >=  b.z - b.depth/2 and a.z - a.depth/2 <= b.z + b.depth/2:
        z_min = True
    if a.z + a.depth/2 >=  b.z - b.depth/2 and a.z - a.depth/2 <= b.z + b.depth/2:
        z_max = True

    # solve
    return (x_min or x_max) and (y_min or y_max) and (z_min or z_max)


def main():
    a = box_collider(0, 0, 0, 1, 1, 1)
    b = box_collider(1, 1, 1, 1, 1, 1)
    collide = check_collision(a,b)
    print(collide)

if __name__ == "__main__":
    main()