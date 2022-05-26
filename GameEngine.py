import pygame as p
from GameObject import GameObject
from Resource import InGameResource
from Components import Camera
from UI import *
class Game:
    # consts
    SIMPLE_SHAPES = GameObject.SIMPLE_SHAPES

    @property
    def my_update(self):
        return self._update()

    @my_update.setter
    def my_update(self, function):
        if callable(function):
            if self.ableCustomUpdate:
                self.update_holder.append(function)
                self.ableCustomUpdate = False
            else:
                raise Exception(f"You already applied custom function to update. Must be only one.")
        else:
            raise Exception(f"Error while trying to add non callable object to update cycle.")

    @property
    def deltaTime(self):
        return self._deltaTime

    @deltaTime.setter
    def deltaTime(self, new):
        raise Exception("This is readonly variable.")

    @deltaTime.getter
    def deltaTime(self):
        fps = self.frameReference.get_fps()
        if fps > 0:
            _deltaTime = 1 / self.frameReference.get_fps()
            return _deltaTime
        else:
            return 0

    @property
    def fps(self):
        return self._fps

    @fps.getter
    def fps(self):
        return self.frameReference.get_fps()

    @fps.setter
    def fps(self, val):
        raise Exception("This is readonly variable.")

    def init(self, screen_size):
        print(f"Game version: " + self.version)
        if type(screen_size) is list and len(screen_size) == 2:
            self.screen = p.display.set_mode([screen_size[0],screen_size[1]])
        elif type(screen_size) is str and 'x' in screen_size:
            self.screen = p.display.set_mode([int(screen_size[:screen_size.find('x')]), int(screen_size[screen_size.find('x')+1:])])
        else:
            raise Exception(f'Screen size must be list [width, size] or "WIDTHxHEIGHT" string. {type(screen_size)} was given.')

    def __init__(self):
        p.init()
        self.version = "dev 0.1"
        self.mainfont = p.font.SysFont("Arial", 24)
        Camera.mainfont = self.mainfont
        self.screen = None

        self.resources = {}
        self.resources_line = ""
        self.resources_text = None

        self.frameReference = p.time.Clock()
        self.update_holder = []
        self.update_holder.append(self.frameReference.tick)
        self.render_queue = []
        self.isFill = True
        self.ableCustomUpdate = True

        self.main_camera = None

        self.show_fps = False

    def run(self):
        running = True
        while running:
            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False
            if self.isFill:
                self.screen.fill((255, 255, 255))
            self._update()

            if self.show_fps:
                t = self.mainfont.render(f"fps:{self.fps//1}", False, (255, 255, 255))
                p.draw.rect(self.screen, (0, 0, 0), t.get_rect())
                self.screen.blit(t, (0, 0))
            p.display.flip()

        p.quit()

    def update_resources(self):
        self.resources_line = ""
        for res in self.resources:
            if not self.resources[res].hide:
                self.resources_line += f"{self.resources[res].name}: {self.resources[res].amount} "
        self.resources_text = self.mainfont.render(self.resources_line, False, (0, 0, 0))

    def _update(self):
        if self.main_camera != None:
            cam = self.main_camera.getComponent("Camera")
            if self.resources_text is not None:
                self.screen.blit(self.resources_text, (0, 0))
            for event in self.update_holder:
                event()
            for info in self.render_queue:
                _info = info()
                if len(_info) > 0:
                    if _info[0]["name"][:2] == "UI":
                        cam.draw(self.screen, _info)
                    elif cam.drawn(_info[0]['obj'].transform.position):
                        cam.draw(self.screen, _info)
        else:
            raise Exception("There is no camera!")

    def add_new_GameObject(self):
        go = GameObject()
        self.update_holder.append(lambda: go.update(self.deltaTime))
        self.render_queue.append(go.draw)
        return go

    def add_new_Resource(self, name):
        r = InGameResource()
        r.name = name
        r.update = self.update_resources
        self.resources[name] = r
        self.update_resources()

    def add_new_UI(self, *args, **kwargs):
        _type = None
        if 'type' in kwargs:
            _type = kwargs['type']
        ui = eval(_type+"()")
        if issubclass(ui.__class__, Label):
            if 'text' in kwargs:
                elem = Label(kwargs['text'], **kwargs)
            else:
                elem = Label("Label", **kwargs)
            self.render_queue.append(elem.draw)
