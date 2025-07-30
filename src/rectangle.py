import pygame
from shape import Shape


class Rectangle(Shape):
    def __init__(self, x, y, width, height, width_limit, height_limit, dt):
        # self.x = x
        # self.y = y - height / 2
        super().__init__(x, y - height / 2)
        self.width = width
        self.height = height
        self.width_limit = width_limit
        self.height_limit = height_limit
        self.dt = dt
       
        
    def is_collision(shape):
        pass
    # def move(self, keys):
    #     if move_direction == "UP":
    #         if self.y > 0:
    #             self.y -= 300 * self.dt
    #         else:
    #             self.y = self.height_limit 
    #     if move_direction == "DOWN":
    #         if self.y < self.height_limit:
    #             self.y += 300 * self.dt
    #         else:
    #             self.y = 0
    #     if move_direction == "LEFT":
    #         if self.x > 0:
    #             self.x -= 300 * self.dt
    #         else:
    #             self.x  = self.wiself.dth_limit
    #     if move_direction == "RIGHT":
    #         if self.x < self.wiself.dth_limit:
    #             self.x += 300 * self.dt
    #         else:
    #             self.x = 0    