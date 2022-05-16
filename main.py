import random as rnd
import GameEngine

game = GameEngine.Game()
game.init("800x600")

game.show_fps = True

game.add_new_Resource("gold")
game.resources["gold"].amount = 1000

points = [(0, 75), (100, 75), (0, 25), (-100, 25)]
obj = game.add_new_GameObject()
obj.transform.position = (200, 200)

obj.addComponent("WiredPolygon")
obj.getComponent("WiredPolygon").points = points

obj.addComponent("Physics2d")
obj.getComponent("Physics2d").applyForce((rnd.randint(-100,100),rnd.randint(-100,100)))
obj.getComponent("Physics2d").mass = rnd.randint(1,10)
obj.getComponent("Physics2d").gravity = True

game.run()