import random as rnd
import GameEngine
import pygame

game = GameEngine.Game()
game.init("800x600")

game.show_fps = True

game.add_new_Resource("gold")
game.resources["gold"].amount = 1000

points = [(0, 5), (5, 10), (10, 5), (10, 0), (0, 0)]
obj = game.add_new_GameObject()
obj.transform.position = (200, 200)

obj.addComponent("WiredPolygon")
obj.getComponent("WiredPolygon").points = points

for i in range(100):
    o2 = game.add_new_GameObject()
    o2.transform.position = (rnd.randint(-1000, 1000), rnd.randint(-1000,1000))
    o2.addComponent("SimpleShape")
    o2.getComponent("SimpleShape").shape = rnd.choice(game.SIMPLE_SHAPES)

game.main_camera = game.add_new_GameObject()
game.main_camera.addComponent("Camera")
game.main_camera.addComponent("WasdControls")

'''obj.addComponent("Physics2d")
obj.getComponent("Physics2d").applyForce((rnd.randint(-100,100),rnd.randint(-100,100)))
obj.getComponent("Physics2d").mass = rnd.randint(1,10)
obj.getComponent("Physics2d").gravity = True'''

game.run()
