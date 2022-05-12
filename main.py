import random as rnd
import GameEngine

game = GameEngine.Game()
game.init("800x600")

game.add_new_Resource("gold")
game.resources["gold"].amount = 1000

for i in range(10):
    obj = game.add_new_GameObject()
    obj.addComponent("Physics2d")
    obj.addComponent("SimpleShape")
    obj.transform.position = (rnd.randint(100,700), 100)

    obj.getComponent("Physics2d").applyForce((rnd.randint(-100,100),rnd.randint(-100,100)))
    obj.getComponent("Physics2d").mass = rnd.randint(1,10)
    obj.getComponent("Physics2d").gravity = True

game.run()