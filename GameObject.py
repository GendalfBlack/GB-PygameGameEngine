import pygame as p
import random as rnd
from Components import *


class GameObject:
    # consts
    SIMPLE_SHAPES = SimpleShape.shapes

    def __init__(self, *args):
        if len(args) == 0:
            self.name = "null"
            self.tag = "null"
        self.components = []
        self.update_holder = []
        self.draw_holder = []
        self.addComponent("Transform")
        self.transform = self.components[0]

    def addComponent(self, component):
        component = eval(component+"()")
        if issubclass(component.__class__, Component):
            self.components.append(component)
            component._owner = self
        else:
            raise Exception('You added non component entity. Inherit "Component" class.')
        if issubclass(component.__class__, BasicComponent):
            if component.update() != 0:
                self.update_holder.append(component.update)
        if issubclass(component.__class__, GraphicComponent):
            self.draw_holder.append(component.draw)

    def update(self, deltaTime):
        for event in self.update_holder:
            if event(deltaTime) != 0:
                return 1
        return 0

    def draw(self):
        render_queue = []
        for event in self.draw_holder:
            render_queue.append(event())
        return render_queue

    def getComponent(self, t):
        for component in self.components:
            if type(component) is eval(t):
                return component
        raise Exception(f"There is no component {t} attached to this object")