from random import randint

def randneg(a):
    r = randint(0, 1)
    if r == 1:
        return a
    else:
        return -a

def positive(a):
    if a >= 0:
        return a
    else:
        return -a

def negative(a):
    if a <= 0:
        return a
    else:
        return -a