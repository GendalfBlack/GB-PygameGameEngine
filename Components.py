# Basic GameObject components
from pygame import Vector2, draw


class Component:
    @property
    def _Owner(self):
        return self._owner

    @_Owner.setter
    def _Owner(self, _object):
        if self._owner is None:
            self._owner = _object
        else:
            raise Exception("You cannot redefine owner of an component")

    @_Owner.getter
    def _Owner(self):
        return self._owner

    def __init__(self, *args, **kargs):
        if len(args) == 0:
            self.name = "Basic component"
        else:
            self.name = args[0]


class BasicComponent(Component):
    def __init__(self, *args, **kargs):
        super(BasicComponent, self).__init__(*args, **kargs)

    def update(self, deltaTime=0):
        pass


class GraphicComponent(Component):
    def __init__(self, *args, **kargs):
        super(GraphicComponent, self).__init__(*args, **kargs)

    def draw(self):
        pass


# 2d
class Transform(BasicComponent):

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if type(value) is tuple:
            self._position.x = value[0]
            self._position.y = value[1]
        elif type(value) is Vector2:
            self._position = value
        else:
            raise Exception(f"Invalid type for position. {type(value)} is provided. Needs to be pair of numbers, or Vector2")

    def __init__(self):
        self._position = Vector2()
        self.rotation = 0
        self.scale = Vector2()
        super().__init__("Transform")

    def update(self, deltaTime=0):
        # print("transform update")
        pass


class Physics2d(BasicComponent):
    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        if type(value) is tuple:
            self._velocity.x = value[0]
            self._velocity.y = value[1]
        elif type(value) is Vector2:
            self._velocity = value
        else:
            raise Exception(
                f"Invalid type for velocity. {type(value)} is provided. Needs to be pair of numbers, or Vector2")

    def __init__(self):
        self._velocity = Vector2()
        self.mass = 1
        self.gravity = False
        super().__init__("Physics2d")

    def update(self, deltaTime=0):
        # print("Physics2d update")
        if self.gravity:
            if self._velocity.y < 98:
                self.applyForce(Vector2(0, 98) * deltaTime * self.mass)
        self._Owner.transform.position += self._velocity * deltaTime

    def applyForce(self, force):
        if type(force) is tuple:
            self._velocity.x += force[0]
            self._velocity.y += force[1]
        elif type(force) is Vector2:
            self._velocity += force
        else:
            raise Exception(f"Can not apply force which not a pair of numbers(tuple), or not a Vector2. {type(force)} was given.")


class BoxCollider(BasicComponent):
    def __init__(self):
        self.size = Vector2()
        self.offset = Vector2()
        super().__init__("BoxCollider")


class SimpleShape(GraphicComponent):
    shapes = ["circle", "square", "line"]

    def __init__(self, shape="circle"):
        self.shape = shape
        self.color = (0, 0, 0)
        self.size = 10
        self.width = 2
        super(SimpleShape, self).__init__("SimpleShape")

    def update(self):
        pass

    def draw(self):
        # print("SimpleShape draw")
        pos = self._Owner.transform.position
        if self.shape == "circle":
            return ["circle", self.color, pos, self.size, self.width]
        elif self.shape == "square":
            x = pos.x; y = pos.y
            rect = (x - self.size / 2, y - self.size / 2, self.size, self.size)
            return ["rect", self.color, rect, self.width]
        elif self.shape == "line":
            x = pos.x; y = pos.y
            p1 = (x - self.size/2, y)
            p2 = (x + self.size/2, y)
            return ["line", self.color, p1, p2, self.width]


class WiredPolygon(GraphicComponent):
    def __init__(self):
        self.points = None
        self.color = (0, 0, 0)
        self.width = 2
        super(WiredPolygon, self).__init__("WiredPolygon")

    def update(self):
        pass

    def draw(self):
        # print("WiredMesh draw")
        lines = []
        pos = self._Owner.transform.position
        for i in range(len(self.points)):
            x1 =0;  x2=0;   y1=0;   y2=0
            if i < len(self.points) - 1:
                x1 = self.points[i][0] + pos.x
                y1 = -self.points[i][1] + pos.y
                x2 = self.points[i+1][0] + pos.x
                y2 = -self.points[i+1][1] + pos.y
            else:
                x1 = self.points[i][0] + pos.x
                y1 = -self.points[i][1] + pos.y
                x2 = self.points[0][0] + pos.x
                y2 = -self.points[0][1] + pos.y
            p1 = (x1, y1)
            p2 = (x2, y2)
            lines.append(["line", self.color, p1, p2, self.width])
        return ["lines", lines]

# 3d
class Camera(BasicComponent):
    def __init__(self):
        self.screen_center = [0, 0]
        self.screen_distance = 100
        super(Camera, self).__init__("Camera")

    def update(self, deltaTime=0):
        pass

    def draw(self, screen):
        pass
