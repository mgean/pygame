import pygame
from shape import Shape


class Rectangle(Shape):
    def __init__(self, x, y, width, height, width_limit, height_limit, dt):
        super().__init__(x, y - height / 2)
        self.width = width
        self.height = height
        self.width_limit = width_limit
        self.height_limit = height_limit
        self.dt = dt
       
        
    def is_collision(self, shape):
        pass