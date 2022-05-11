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
        self._owner = None
        if len(args) == 0:
            self.name = "Basic component"
        else:
            self.name = args[0]
        if "owner" in kargs:
            self._Owner = kargs["owner"]
        else:
            raise Exception(f"There is no owner for this component. {self.name}")


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
    def __init__(self, _object):
        self.position = Vector2()
        self.rotation = 0
        self.scale = Vector2()
        super().__init__("Transform", owner=_object)

    def update(self, deltaTime=0):
        # print("transform update")
        pass


class Physics2d(BasicComponent):
    def __init__(self, _object):
        self.velocity = Vector2()
        super().__init__("Physics2d", owner=_object)

    def update(self, deltaTime=0):
        # print("Physics2d update")
        self._Owner.transform.position += self.velocity * deltaTime


class SimpleShape(GraphicComponent):
    def __init__(self, _object, shape="circle"):
        self.shape = shape
        self.color = (0, 0, 0)
        self.size = 10
        self.rect = None
        super(SimpleShape, self).__init__("SimpleShape", owner=_object)

    def update(self):
        pass

    def draw(self, screen):
        if self.shape == "circle":
            self.rect = eval("draw."+self.shape+"(screen, self.color, self._Owner.transform.position, self.size)")