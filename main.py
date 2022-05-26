import random as rnd
import GameEngine
import pygame

game = GameEngine.Game()
game.init("800x600")

game.show_fps = True

game.add_new_Resource("gold")
game.resources["gold"].amount = 1000

for i in range(1000):
    o2 = game.add_new_GameObject()
    o2.transform.position = (rnd.randint(-1000, 1000), rnd.randint(-1000,1000))
    o2.addComponent("SimpleShape")
    o2.getComponent("SimpleShape").shape = rnd.choice(game.SIMPLE_SHAPES)
    o2.getComponent("SimpleShape").color = rnd.choice(["red", "green","blue", "yellow"])
    #o2.addComponent("OnClick")

game.main_camera = game.add_new_GameObject()
game.main_camera.addComponent("Camera")
game.main_camera.addComponent("WasdControls")

game.run()
