# Separating Axis Theorem

import math

class vec2:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'x='+str(self.x)+' y='+str(self.y)
    def __str__(self):
        return 'x='+str(self.x)+' y='+str(self.y)
    def __add__(self,o):
        return vec2(self.x + o.x, self.y + o.y)
    def __sub__(self,o):
        return vec2(self.x - o.x, self.y - o.y)

def v2_normalise(a):
    l = a.x * a.x + a.y * a.y
    r = math.sqrt(l)
    return vec2(a.x / r, a.y / r)

def v2_perp(a):
    return vec2(-a.y, a.x)


class mat2:
    def __init__(self,a=1,b=0,c=0,d=1):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.m = [a,b,c,d]
    
def m2_inverse(m):
    return m2_mul_f(mat2(m.d, -m.b, -m.c, m.a), m2_determinant(m))

def m2_determinant(m):
    d = m.a*m.d-m.b*m.c
    if d != 0:
        return 1/d
    else:
        return 0

def m2_mul_f(m, f):
    return mat2(m.a*f, m.b*f, m.c*f, m.d*f)

def m2_mul_v2(m, v):
    return vec2(m.a*v.x + m.b*v.y, m.c*v.x + m.d*v.y)


class square_collider:

    def __init__(self,pos=vec2(),rot=0,scl=vec2(1,1)):
        self.pos = pos
        self.rot = rot
        self.scl = scl

    def get_points(self):
        points = []
        l = math.sqrt(self.scl.x * self.scl.y)
        for theta in range(0, 360, 90):
            points.append(vec2(
                    l * (1/math.sqrt(2)) * math.cos(math.radians(self.rot + 45 + theta)) + self.pos.x,       # x
                    l * (1/math.sqrt(2)) * math.sin(math.radians(self.rot + 45 + theta)) + self.pos.y        # y
                )
            )
        return points

def check_collision(a, b):
    a_points = a.get_points()
    b_points = b.get_points()
    
    vecs = [
        v2_normalise(a_points[0] - a_points[1]), 
        v2_normalise(a_points[0] - a_points[3])
    ]
    perps = [ v2_perp(vecs[0]), v2_perp(vecs[1]) ]

    lambdas = {"min": None, "max": None, "list": []}
    
    line_mat = mat2(vecs[0].x, -perps[0].x, vecs[0].y, -perps[0].y)
    inv_mat = m2_inverse(line_mat)

    print("a")
    for point in a_points:
        unknown = m2_mul_v2(inv_mat, point)
        lambdas["list"].append(unknown.x)
        # compare min
        if not lambdas["min"]:
            lambdas["min"] = unknown.x
        elif unknown.x < lambdas["min"]:
            lambdas["min"] = unknown.x
        # compare max
        if not lambdas["max"]:
            lambdas["max"] = unknown.x
        elif unknown.x > lambdas["max"]:
            lambdas["max"] = unknown.x
        print(unknown.x)
    
    isColliding = False
    print("b")
    for point in b_points:
        unknown = m2_mul_v2(inv_mat, point)
        print(unknown.x)
        if unknown.x >= lambdas["min"] and unknown.x <= lambdas["max"]:
            isColliding = True

    if isColliding:
        print("mmmh touch")
    else:
        print("no me gusta")

    # MATHS
    # x_vec * lambda - x_perp * gamma = point.x

    # x_vec.x * lambda - x_perp.x * gamma = point.x
    # x_vec.y * lambda - x_perp.y * gamma = point.y

    # | vx  -px |   | L |   | pX |
    # | vy  -py | * | G | = | pY |

def rad(deg):
    return deg * math.pi / 180


def main():
    box = square_collider()
    box_box = square_collider(vec2(1,1))
    check_collision(box, box_box)

if __name__ == "__main__":
    main()