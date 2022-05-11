import pygame as p
import GameEngine

p.init()
s = p.display.set_mode([800,600])

game = GameEngine.Game()
game.init(s)
obj = game.add_new_GameObject()
obj.addComponent("Physics2d")
obj.addComponent("SimpleShape")
obj.transform.position = p.Vector2(100, 100)
obj.components[1].velocity = p.Vector2(50, 50)

running = True
while running:
    for e in p.event.get():
        if e.type == p.QUIT:
            running = False
    s.fill((255,255,255))
    game.update()
    p.display.flip()

p.quit()