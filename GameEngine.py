import pygame as p

class Game:

    def __init__(self):
        self.version = "0.1"
        self.mainfont = p.font.SysFont("Consolas", 24)
        self.frameReference = p.time.Clock()

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

    def init(self):
        print(f"Game version: " + self.version)

    def Frame(self):
        self.frameReference.tick()