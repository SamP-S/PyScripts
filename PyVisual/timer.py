# standard module
import time

# timer class 
class timer:
    # starts the timer when the object is created
    def __init__(self):
        self.start = time.time()
    # gets the time ellased since starting
    # isMilli determines if the return result 
    # is milliseconds or seconds
    def get_time(self, isMilli=False):
        if isMilli:
            return (time.time() - self.start) * 1000
        else:
            return time.time() - self.start
    # resets the timer to 0
    def reset(self):
        self.start = time.time()
