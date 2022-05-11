import pygame as p
import random as rnd
from Vector2d import Vector

class GameObject:
    def __init__(self, *args):
        if len(args) == 0:
            self.name = "null"
            self.tag = "null"
            self.cords = Vector()
