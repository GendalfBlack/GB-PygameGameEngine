import pygame as p
import GameEngine
p.init()
s = p.display.set_mode([800,600])

g = GameEngine.Game()
g.init()

running = True
while running:
    for e in p.event.get():
        if e.type == p.QUIT:
            running = False
    s.fill((255,255,255))
    p.display.flip()

p.quit()