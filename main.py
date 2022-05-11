import pygame as p
import GameEngine
from Components import *

p.init()
s = p.display.set_mode([800,600])

game = GameEngine.Game()
game.init(s)
obj = game.add_new_GameObject()
obj.addComponent(Physics2d(obj))
obj.addComponent(SimpleShape(obj))
obj.transform.position.x = 100
obj.transform.position.y = 100

running = True
while running:
    for e in p.event.get():
        if e.type == p.QUIT:
            running = False
    s.fill((255,255,255))
    game.update()
    p.display.flip()

p.quit()