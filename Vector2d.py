class Vector:
    def __init__(self, *args):
        if len(args) == 0:
            self.x = 0
            self.y = 0
        if len(args) == 2:
            self.x = args[0]
            self.y = args[1]

    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    def len(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __mul__(self, s):
        return Vector(self.x * s, self.y * s)

    def norm(self):
        l = self.len()
        self.x *= 1 / l
        self.y *= 1 / l
