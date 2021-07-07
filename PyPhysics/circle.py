import math

def printf(f):
    print("%.1f" % f, end="")

def abs(a):
    if a >= 0:
        return a
    return -a

class Circle:

    def __init__(self, _x, _y, _r, _vx, _vy, _colour):
        self.x = _x
        self.y = _y
        self.r = abs(_r)
        self.vx = _vx
        self.vy = _vy
        self.colour = _colour

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def min_x(self):
        return self.x - self.r
    
    def max_x(self):
        return self.x + self.r

    def min_y(self):
        return self.y - self.r

    def max_y(self):
        return self.y + self.r

def check_circle_collision(a, b):
    dx = a.x - b.x
    dy = a.y - b.y
    hyp2 = dx * dx + dy * dy
    thresh = a.r + b.r
    if hyp2 < thresh * thresh:
        return True
    else:
        return False

# https://www.vobarian.com/collisions/2dcollisions2.pdf
def handle_circle_collision(a, b):

    # get mass
    ma = a.r
    mb = b.r
    mt = ma + mb

    # calculate positional difference
    dx = a.x - b.x
    dy = a.y - b.y

    # get distances
    dist = math.sqrt(dx * dx + dy * dy)
    max_dist = a.r + b.r
    dd = max_dist - dist

    # get normal vector
    unx = dx / dist
    uny = dy / dist

    # get tangent vector
    utx = -uny
    uty = unx
    
    # ccw angle between a & b
    theta = math.atan2(dy, dx)
    

    # print("vel a:", a.vx, a.vy, math.sqrt(a.vx*a.vx + a.vy*a.vy))
    # print("vel b:", b.vx, b.vy, math.sqrt(b.vx*b.vx + b.vy*b.vy))

    # # calculate start vector for validation
    # start_vel_a = math.sqrt(a.vx * a.vx + a.vy * a.vy)
    # start_vel_b = math.sqrt(b.vx * b.vx + b.vy * b.vy)
    # start_mom = 0.5 * ma * start_vel_a * start_vel_a + 0.5 * mb * start_vel_b * start_vel_b
    
    
    # calculate current tangent velocity
    vat = a.vx * utx + a.vy * uty
    vbt = b.vx * utx + b.vy * uty

    # calculate current normal velocity
    van = a.vx * unx + a.vy * uny
    vbn = b.vx * unx + b.vy * uny

    # calculate response tangent velocity
    vat2 = vat
    vbt2 = vbt

    # calculate response normal velocity
    van2 = (van * (ma - mb) + 2 * mb * vbn) / (ma + mb)
    vbn2 = (vbn * (mb - ma) + 2 * ma * van) / (ma + mb)

    # convert tangent velocity to components
    vat2x = vat2 * utx
    vat2y = vat2 * uty
    vbt2x = vbt2 * utx
    vbt2y = vbt2 * uty

    # convert normal velocity to components
    van2x = van2 * unx
    van2y = van2 * uny
    vbn2x = vbn2 * unx
    vbn2y = vbn2 * uny

    # combine normal and tangents to total response velocities by component
    vax2 = vat2x + van2x
    vay2 = vat2y + van2y
    vbx2 = vbt2x + vbn2x
    vby2 = vbt2y + vbn2y
    
    # assign to objects
    a.vx = vax2
    a.vy = vay2
    b.vx = vbx2
    b.vy = vby2

    # move objects outside eachother
    a.x  += dd * math.cos(theta) * ma / mt
    a.y  += dd * math.sin(theta) * ma / mt
    b.x  += -dd * math.cos(theta) * mb / mt
    b.y  += -dd * math.sin(theta) * mb / mt


    # # calculate end vector for validation
    # end_vel_a = math.sqrt(a.vx * a.vx + a.vy * a.vy)
    # end_vel_b = math.sqrt(b.vx * b.vx + b.vy * b.vy)
    # end_mom = 0.5 * ma * end_vel_a * end_vel_a + 0.5 * mb * end_vel_b * end_vel_b

    
    # if start_mom - end_mom < 0.0001:
    #     print("cool")
    # else:
    #     print("start mom:", start_mom)
    #     print("end mom:", end_mom)
    #     print("WAAAAAAAAAAAAAAAAH")
    #     # print("delta:", dx, dy)
    #     # print("theta:", theta)
    #     print(math.sqrt(unx*unx + uny*uny))
    #     print(math.sqrt(utx*utx + uty*uty))
    #     print()
    #     print("mass:", ma, "\t",  mb, "\t",  ma + mb)
    #     print("tangent:", vat, "\t", vbt, "\t", vat + vbt)
    #     print("tangent1:", vat2, "\t",  vbt2, "\t",  vat2 + vbt2)
    #     print("normal:", van, "\t",  vbn, "\t",  van + vbn)
    #     print("normal2:", van2, "\t",  vbn2, "\t",  van2 + vbn2)
    #     print()
    #     print("vel a:", a.vx, "\t",  a.vy, "\t",  math.sqrt(a.vx*a.vx + a.vy*a.vy))
    #     print("vel b:", b.vx, "\t",  b.vy, "\t",  math.sqrt(b.vx*b.vx + b.vy*b.vy))
    #     print()


def main():
    a = Circle(2, 3, 3)
    b = Circle(-1, -2, 2)
    print(check_circle_collision(a, b))

if __name__ == "__main__":
    main()
