import math
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def distance_from_origin(self):
        return math.hypot(self.x, self.y)
    
    def __eq__(self, other):
        