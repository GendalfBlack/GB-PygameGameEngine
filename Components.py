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

    def draw(self, screen):
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
        self.rect = None
        self.width = 2
        super(SimpleShape, self).__init__("SimpleShape")

    def update(self):
        pass

    def draw(self, screen):
        # print("SimpleShape draw")
        if self.shape == "circle":
            pos = self._Owner.transform.position
            self.rect = eval("draw.circle(screen, self.color, pos, self.size, width=self.width)")
        elif self.shape == "square":
            x = self._Owner.transform.position.x
            y = self._Owner.transform.position.y
            rect = (x - self.size / 2, y - self.size / 2, self.size, self.size)
            self.rect = eval("draw.rect(screen, self.color, rect, width=self.width)")
        elif self.shape == "line":
            x = self._Owner.transform.position.x
            y = self._Owner.transform.position.y
            self.rect = eval("draw.line(screen, self.color, (x - self.size/2, y), (x + self.size/2, y), width=self.width)")