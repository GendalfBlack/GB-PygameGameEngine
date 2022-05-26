from pygame import Vector2


class UI:
    def __init__(self, name):
        self.name = "UI." + name
        self.position = Vector2(0,0)


class Label(UI):
    def __init__(self, *args, **kwargs):
        super().__init__("Label")
        self.text = ""
        self.color = "black"
        if len(args) > 0:
            self.text = args[0]
        if 'pos' in kwargs:
            self.position = kwargs['pos']
        if 'color' in kwargs:
            self.color = kwargs['color']

    def draw(self):
        return [{"name": self.name, "text": self.text, "pos": self.position, "color": self.color}]