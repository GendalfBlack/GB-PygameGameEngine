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
            self.update_holder.append(component.update)
        if issubclass(component.__class__, GraphicComponent):
            self.draw_holder.append(component.draw)

    def update(self, deltaTime):
        for event in self.update_holder:
            event(deltaTime)

    def draw(self, screen):
        for event in self.draw_holder:
            event(screen)

    def getComponent(self, t):
        for component in self.components:
            if type(component) is eval(t):
                return component
        raise Exception(f"There is no component {t} attached to this object")