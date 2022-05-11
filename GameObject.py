import pygame as p
import random as rnd
from Components import *


class GameObject:
    def __init__(self, *args):
        if len(args) == 0:
            self.name = "null"
            self.tag = "null"
        self.components = [Transform(self)]
        self.transform = self.components[0]
        self.update_holder = [self.transform.update]
        self.draw_holder = []

    def addComponent(self, component):
        if issubclass(component.__class__, Component):
            self.components.append(component)
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