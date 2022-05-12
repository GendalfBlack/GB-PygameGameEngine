import GameEngine

game = GameEngine.Game()
game.init("800x600")
obj = game.add_new_GameObject()
obj.addComponent("Physics2d")
obj.addComponent("SimpleShape")
obj.transform.position = (100, 100)
obj.components[1].velocity = (50, 50)

game.run()