from shape import Shape
from rectangle import Rectangle
import math


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius


    def is_collision(self, target):
        result = False
        if isinstance(target, Rectangle):
            # use point vs circle detection
            cx = self.x
            cy = self.y
            px = max(target.x, min(cx, target.x + target.width))
            py = max(target.y, min(cy, target.y + target.height))            
            distance = math.sqrt((cx - px)**2 + (cy - py)**2)
            result = distance <= self.radius
        else:
            print("not supported")
        
        
        return result