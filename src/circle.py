from shape import Shape


class Circle(Shape):
    def __init__(self, x, y, radius):
        # self.x = x
        # self.y = y
        super().__init__(x, y)
        self.radius = radius


    def is_collision(shape):
        pass