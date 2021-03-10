import math

# 2x2 mat

class mat2:
    def __init__(self, m00=1, m01=0, m10=0, m11=1):
        self.m00 = m00
        self.m01 = m01
        self.m10 = m10
        self.m11 = m11
        self.m = [m00, m01, m10, m11]

    # string return for printing
    def __str__(self):
        return "m2: " + str([self.m00, self.m01]) + "/n    " + str([self.m10, self.m11])

    # overload + operator
    def __add__(self, m):
        return mat2(self.m00 + m.m00, self.m01 + m.m01, self.m10 + m.m10, self.m11 + m.m11)
    # overload - operator
    def __sub__(self, m):
        return mat2(self.m00 - m.m00, self.m01 - m.m01, self.m10 - m.m10, self.m11 - m.m11)
    # overload * operator
    def __mul__(self, m):
        return mat2(self.m00 * m.m00, self.m01 * m.m01, self.m10 * m.m10, self.m11 * m.m11)
    # overload / operator
    # __floordiv__ or __truediv__

    # overload == operators
    def __eq__(self, m):
        return self.m == m.m
    # overload != operators
    def __ne__(self, m):
        return self.m != m.m

    @property
    def divw(self):
        if self.m11 == 0:
            return self
        return mat2(self.m00/self.m11, self.m01/self.m11, self.m10/self.m11, self.m11/self.m11)
    @property
    def abs(self):
        return mat2(abs(self.m00), abs(self.m01), abs(self.m10), abs(self.m11))

    @property
    def pos(self):
        return mat2(max(self.m00, 0), max(self.m01, 0), max(self.m10, 0), max(self.m11, 0))
    @property
    def neg(self):
        return mat2(min(self.m00, 0), min(self.m01, 0), min(self.m10, 0), min(self.m11, 0))

    @property
    def col(self, i):
        return [self.m[0+i], self.m[2+i]]
    @property
    def row(self, j):
        return [self.m[j*2+0], self.m[j*2+1]]

    @property
    def arr1d(self):
        return self.m
    @property
    def arr2d(self):
        return [[self.m00, self.m01], [self.m10, self.m11]]


# 3x3 mat

#


# 4x4 mat

class mat4:
    def __init__(self, m00=1, m01=0, m02=0, m03=0, m10=0, m11=1, m12=0, m13=0, m20=0, m21=0, m22=1, m23=0, m30=0, m31=0, m32=0, m33=1):
        self.m00 = m00; self.m01 = m01; self.m02 = m02; self.m03 = m03
        self.m10 = m10; self.m11 = m11; self.m12 = m12; self.m13 = m13
        self.m20 = m20; self.m21 = m21; self.m22 = m22; self.m23 = m23
        self.m30 = m30; self.m31 = m31; self.m32 = m32; self.m33 = m33
        self.m = [  m00, m01, m02, m03, 
                    m10, m11, m12, m13, 
                    m20, m21, m22, m23, 
                    m30, m31, m32, m33  ]

    # string return for printing
    def __str__(self):
        return "m2: " + str([self.m00, self.m01]) + "/n    " + str([self.m10, self.m11])

    # overload + operator
    def __add__(self, m):
        return mat2(self.m00 + m.m00, self.m01 + m.m01, self.m10 + m.m10, self.m11 + m.m11)
    # overload - operator
    def __sub__(self, m):
        return mat2(self.m00 - m.m00, self.m01 - m.m01, self.m10 - m.m10, self.m11 - m.m11)
    # overload * operator
    def __mul__(self, m):
        return mat2(self.m00 * m.m00, self.m01 * m.m01, self.m10 * m.m10, self.m11 * m.m11)
    # overload / operator
    # __floordiv__ or __truediv__

    # overload == operators
    def __eq__(self, m):
        return self.m == m.m
    # overload != operators
    def __ne__(self, m):
        return self.m != m.m

    @property
    def divw(self):
        if self.m11 == 0:
            return self
        return mat2(self.m00/self.m11, self.m01/self.m11, self.m10/self.m11, self.m11/self.m11)
    @property
    def abs(self):
        return mat2(abs(self.m00), abs(self.m01), abs(self.m10), abs(self.m11))

    @property
    def pos(self):
        return mat2(max(self.m00, 0), max(self.m01, 0), max(self.m10, 0), max(self.m11, 0))
    @property
    def neg(self):
        return mat2(min(self.m00, 0), min(self.m01, 0), min(self.m10, 0), min(self.m11, 0))
    
    @property
    def col(self, i):
        return [self.m[0+i], self.m[4+i], self.m[8+i], self.m[12+i]]
    @property
    def row(self, j):
        return [self.m[j*4+0], self.m[j*4+1], self.m[j*4+2], self.m[j*4+3]]

    @property
    def arr1d(self):
        return self.m
    @property
    def arr2d(self):
        return [[self.m00, self.m01], [self.m10, self.m11]]