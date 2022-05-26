# Basic GameObject components
import pygame
from pygame import Vector3, draw, key


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
        return 0


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
        elif type(value) is Vector3:
            self._position = value
        else:
            raise Exception(f"Invalid type for position. {type(value)} is provided. Needs to be pair of numbers, or Vector2")

    def __init__(self):
        self._position = Vector3()
        self.rotation = 0
        self.scale = Vector3()
        super().__init__("Transform")

    def update(self, deltaTime=0):
        # print("transform update")
        return 1


class Physics2d(BasicComponent):
    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        if type(value) is tuple:
            self._velocity.x = value[0]
            self._velocity.y = value[1]
        elif type(value) is Vector3:
            self._velocity = value
        else:
            raise Exception(
                f"Invalid type for velocity. {type(value)} is provided. Needs to be pair of numbers, or Vector2")

    def __init__(self):
        self._velocity = Vector3()
        self.mass = 1
        self.gravity = False
        super().__init__("Physics2d")

    def update(self, deltaTime=0):
        # print("Physics2d update")
        if self.gravity:
            if self._velocity.y > -98:
                self.applyForce(Vector3(0, -98, 0) * deltaTime * self.mass)
        if self._velocity.x > 0.01 or self._velocity.x < -0.01:
            if self._velocity.y > 0.01 or self._velocity.y < -0.01:
                self._Owner.transform.position += self._velocity * deltaTime
        return 1

    def applyForce(self, force):
        if type(force) is tuple:
            self._velocity.x += force[0]
            self._velocity.y += force[1]
        elif type(force) is Vector3:
            self._velocity += force
        else:
            raise Exception(f"Can not apply force which not a pair of numbers(tuple), or not a Vector2. {type(force)} was given.")


class BoxCollider(BasicComponent):
    def __init__(self):
        self.size = Vector3()
        self.offset = Vector3()
        super().__init__("BoxCollider")


class SimpleShape(GraphicComponent):
    shapes = ["circle", "square", "line"]

    def __init__(self, shape="circle"):
        self.shape = shape
        self.color = (0, 0, 0)
        self.size = 10
        self.width = 2
        super(SimpleShape, self).__init__("SimpleShape")

    def draw(self):
        # print("SimpleShape draw")
        pos = self._Owner.transform.position
        if self.shape == "circle":
            return {"obj": self._Owner, "name": "circle", "color": self.color, 2: pos, 3: self.size/2, 4: self.width}
        elif self.shape == "square":
            x = pos.x; y = pos.y
            rect = (x - self.size / 2, y - self.size / 2, self.size, self.size)
            return {"obj": self._Owner, "name":"rect", "color":self.color, 2:rect, 3:self.width}
        elif self.shape == "line":
            x = pos.x; y = pos.y
            p1 = (x - self.size/2, y)
            p2 = (x + self.size/2, y)
            return {"obj": self._Owner, "name":"line", "color":self.color, 2:p1, 3:p2, 4:self.width}


class WiredPolygon(GraphicComponent):
    def __init__(self):
        self.points = None
        self.color = (0, 0, 0)
        self.width = 2
        super(WiredPolygon, self).__init__("WiredPolygon")

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
            lines.append({"obj": self._Owner,"name":"line", "color":self.color, 2:p1, 3:p2, 4:self.width})
        return {"obj": self._Owner,"name":"lines", 1:lines}


# 3d
class Camera(BasicComponent):
    mainfont = None

    def __init__(self):
        self.screen_center = [0, 0]
        self.screen_distance = 100
        super(Camera, self).__init__("Camera")

    def update(self, deltaTime=0):
        return 0

    def drawn(self, pos):
        p = self._Owner.transform.position
        if 800 > pos[0] + p.x > 0 and 600 > pos[1] + p.y > 0:
            return True
        return False

    def draw(self, screen, objects):
        # print("Camera draw")
        pos = self._Owner.transform.position
        for _object in objects:
            if _object["name"] == 'lines':
                for line in _object[1]:
                    if self.drawn(line[2]) and self.drawn(line[3]):
                        p1 = (line[2][0] + pos.x, line[2][1] + pos.y)
                        p2 = (line[3][0] + pos.x, line[3][1] + pos.y)
                        draw.line(screen, line["color"], p1, p2, width=line[4])
            if _object["name"] == "line":
                if self.drawn(_object[2]) and self.drawn(_object[3]):
                    p1 = (_object[2][0] + pos.x, _object[2][1] + pos.y)
                    p2 = (_object[3][0] + pos.x, _object[3][1] + pos.y)
                    draw.line(screen, _object["color"], p1, p2, width=_object[4])
            if _object["name"] == "circle":
                if self.drawn(_object[2]):
                    p1 = (_object[2][0] + pos.x, _object[2][1] + pos.y)
                    draw.circle(screen, _object["color"], p1, _object[3], _object[4])
            if _object["name"] == "rect":
                if self.drawn((_object[2][0],_object[2][1])):
                    r = (_object[2][0] + pos.x, _object[2][1] + pos.y, _object[2][2], _object[2][3])
                    draw.rect(screen, _object["color"], r, _object[3])
            if _object["name"] == "UI.Label":
                f = Camera.mainfont
                t = f.render(_object["text"], False, _object["color"])
                screen.blit(t, (_object["pos"][0], _object["pos"][1]))
        return 1


class WasdControls(BasicComponent):
    def __init__(self):
        self.enabled = True
        self.vertical = "y"
        self.horizontal = "x"
        self.speed = 200
        super(WasdControls, self).__init__("WasdControls")

    def update(self, deltaTime=0):
        # print("WasdControls update")
        k = key.get_pressed()
        _object = self._Owner.transform.position
        if k[pygame.K_a]:
            _object.x += self.speed * deltaTime
        if k[pygame.K_d]:
            _object.x -= self.speed * deltaTime
        if k[pygame.K_w]:
            _object.y += self.speed * deltaTime
        if k[pygame.K_s]:
            _object.y -= self.speed * deltaTime


class OnClick(BasicComponent):
    def __init__(self):
        self.enabled = True
        self.screen_pos = Vector3()
        super(OnClick, self).__init__("OnClick")

    def update(self, deltaTime=0):
        print(pygame.mouse.get_pos())
        if pygame.mouse.get_pos()[0]== screen_pos.x and pygame.mouse.get_pos()[1] == screen_pos.y:
            print("OnClick")
