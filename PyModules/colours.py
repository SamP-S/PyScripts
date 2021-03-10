
# basic class to store colour information
# each colour element is individually addressable
# has tuple return functions
class colour:
    # initilisation method requires r,g,b values
    # else just use standard colours
    def __init__(self, r, g, b, a=255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.__value = (self.r, self.g, self.b, self.a)
    # returns tuple of rgb values
    def rgb(self):
        return (self.r, self.g, self.b)
    # returns tuple of rgba values
    def rgba(self):
        return (self.r, self.g, self.b, self.a)

# dictionary of standard colours using the colour class
# all lower case
COLOURS = {
    # 1-colour
    "red"       : colour(255, 0, 0),
    "green"     : colour(0, 255, 0),
    "blue"      : colour(0, 0, 255),
    # 2-colour
    "yellow"    : colour(255, 255, 0),
    "cyan"      : colour(0, 255, 255),
    "magenta"   : colour(255, 0, 255),
    # 3-colour
    "white"     : colour(255, 255, 255),
    "black"     : colour(0, 0, 0)
}