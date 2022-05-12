import pygame as p
from GameObject import GameObject

class Game:

    def __init__(self):
        p.init()
        self.version = "dev 0.1"
        self.mainfont = p.font.SysFont("Consolas", 24)

        self.screen = None

        self.frameReference = p.time.Clock()
        self.update_holder = []
        self.update_holder.append(self.frameReference.tick)
        self.draw_holder = []
        self.ableCustomUpdate = True

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

    def run(self):
        running = True
        while running:
            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False
            self.screen.fill((255, 255, 255))
            self._update()
            p.display.flip()

        p.quit()

    def _update(self):
        for event in self.update_holder:
            event()
        for draw in self.draw_holder:
            draw()

    def add_new_GameObject(self):
        go = GameObject()
        self.update_holder.append(lambda : go.update(self.deltaTime))
        self.draw_holder.append(lambda : go.draw(self.screen))
        return go
