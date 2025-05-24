from math import *
import numpy as np

# support functions
def pos(a):
    if a >= 0:
        return a
    else:
        return -a

def neg(a):
    if a <= 0:
        return a
    else:
        return -a
    
# numerical methods for ordinary differential equations

# https://en.wikipedia.org/wiki/Euler_method
# explicit, as solution for yn+1 is a function of yi for i <= n
# given a t0, y0=y(t0) and y'(t) = f(t, y(t))
# h is step size
# tn = t0 + n * h || tn+1 = tn + h
# yn+1 = yn + h * f(tn, yn)
# such that yn ~ y(tn)
def euler(func, t0, y0, h):
    yn = y0 + h * func(t0, y0)
    tn = t0 + h
    return tn, yn

def midpoint():
    pass

# numerical methods for partial differential equations
# TODO

if __name__ == "__main__":
    
    
    
    # linear equation y = m*x + c
    # y = 2x + 1
    # dy/dx = 2
    def func(t, y):
        return 2
    
    # quadratic formula y = a*x^2 + b*x + c
    # y = 0.5x^2 - 4x
    # dy/dx = x - 4
    def func(t, y):
        return t - 4

    STEPS = 10
    t = np.zeros((STEPS))
    y = np.zeros((STEPS))  
    
    # start
    t[0] = 0.0
    y[0] = 0.0
    for i in range(1, STEPS):
        t[i], y[i] = euler(func, t[i-1], y[i-1], 1)
        
    
    # debug
    print(f"t: {t}")
    print(f"y: {y}")    