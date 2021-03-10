import math

# 2D - Vector

class vec2:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.v = [self.x, self.y]

    # string return for printing
    def __str__(self):
        return "v2: x=" + str(self.x) + "  y=" + str(self.y)

    # overload + operator
    def __add__(self, v):
        return vec2(self.x + v.x, self.y + v.y)
    # overload - operator
    def __sub__(self, v):
        return vec2(self.x - v.x, self.y - v.y)
    # overload * operator
    def __mul__(self, v):
        return vec2(self.x * v.x, self.y * v.y)
    # overload / operator
    # __floordiv__ or __truediv__

    # overload == operators
    def __eq__(self, v):
        return self.x == v.x and self.y == v.y
    # overload != operators
    def __ne__(self, v):
        return self.x != v.x or self.y != v.y


    @property
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
    
    @property
    def normalised(self):
        l = self.length
        return vec2(self.x / l, self.y / l)

    @property
    def abs(self):
        return vec2(abs(self.x), abs(self.y))

    @property
    def pos(self):
        return vec2(max(self.x, 0), max(self.y, 0))
    @property
    def neg(self):
        return vec2(min(self.x, 0), min(self.y, 0))

    @property
    def min(self):
        return min(self.x, self.y)
    @property
    def max(self):
        return max(self.x, self.y)

    @property
    def tup(self):
        return (self.x, self.y)
    @property
    def arr(self):
        return [self.x, self.y]


# 3D - vector

class vec3:
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
        self.v = [self.x, self.y, self.z]

    # string return for printing
    def __str__(self):
        return "v3: x=" + str(self.x) + "  y=" + str(self.y) + "  z=" + str(self.z)

    # overload + operator
    def __add__(self, v):
        return vec3(self.x + v.x, self.y + v.y, self.z + v.z)
    # overload - operator
    def __sub__(self, v):
        return vec3(self.x - v.x, self.y - v.y, self.z - v.z)
    # overload * operator
    def __mul__(self, v):
        return vec3(self.x * v.x, self.y * v.y, self.z * v.z)
    # overload / operator
    # __floordiv__ or __truediv__

    # overload == operators
    def __eq__(self, v):
        return self.x == v.x and self.y == v.y and self.z == v.z
    # overload != operators
    def __ne__(self, v):
        return self.x != v.x or self.y != v.y and self.z != v.z


    @property
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    
    @property
    def normalised(self):
        l = self.length
        return vec3(self.x / l, self.y / l, self.z / l)

    @property
    def abs(self):
        return vec3(abs(self.x), abs(self.y), abs(self.z))

    @property
    def pos(self):
        return vec3(max(self.x, 0), max(self.y, 0), max(self.z, 0))
    @property
    def neg(self):
        return vec3(min(self.x, 0), min(self.y, 0), min(self.z, 0))

    @property
    def min(self):
        return min(self.x, self.y, self.z)
    @property
    def max(self):
        return max(self.x, self.y, self.z)

    @property
    def tup(self):
        return (self.x, self.y, self.z)
    @property
    def arr(self):
        return [self.x, self.y, self.z]


# 4D - vector

class vec4:
    def __init__(self,x=0,y=0,z=0,w=1):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.v = [self.x, self.y, self.z, self.w]

    # string return for printing
    def __str__(self):
        return "v4: x=" + str(self.x) + "  y=" + str(self.y) + "  z=" + str(self.z) + "  w=" + str(self.w)

    # overload + operator
    def __add__(self, v):
        return vec4(self.x + v.x, self.y + v.y, self.z + v.z, self.w + self.w)
    # overload - operator
    def __sub__(self, v):
        return vec4(self.x - v.x, self.y - v.y, self.z - v.z, self.w - v.w)
    # overload * operator
    def __mul__(self, v):
        return vec4(self.x * v.x, self.y * v.y, self.z * v.z, self.w * v.w)
    # overload / operator
    # __floordiv__ or __truediv__

    # overload == operators
    def __eq__(self, v):
        return self.x == v.x and self.y == v.y and self.z == v.z and self.w == v.w
    # overload != operators
    def __ne__(self, v):
        return self.x != v.x or self.y != v.y and self.z != v.z and self.w != v.w


    @property
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z + self.w * self.w)
    
    @property
    def normalised(self):
        l = self.length
        return vec4(self.x / l, self.y / l, self.z / l, self.w / l)

    @property
    def abs(self):
        return vec4(abs(self.x), abs(self.y), abs(self.z), abs(self.w))

    @property
    def pos(self):
        return vec4(max(self.x, 0), max(self.y, 0), max(self.z, 0), max(self.w, 0))
    @property
    def neg(self):
        return vec4(min(self.x, 0), min(self.y, 0), min(self.z, 0), min(self.w, 0))

    @property
    def min(self):
        return min(self.x, self.y, self.z, self.w)
    @property
    def max(self):
        return max(self.x, self.y, self.z, self.w)

    @property
    def tup(self):
        return (self.x, self.y, self.z, self.w)
    @property
    def arr(self):
        return [self.x, self.y, self.z, self.w]