from time import time_ns
from enum import Enum

# timer class 
class Timer:
    
    class Unit(Enum):
        s = 3
        ms = 2
        us = 1
        ns = 0
    
    # create timer object
    def __init__(self):
        self.start = time_ns()
        
    # gets the time ellased since starting
    def get_time(self, unit=Unit.s):
        return (time_ns() - self.start) / pow(10, unit * 3)
    
    # resets the timer to 0
    def reset(self):
        self.start = time_ns()
