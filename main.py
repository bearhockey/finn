import os

import settings
from src.Board import Board
from src.Game import Game
from src.Title import Title

# if __name__ == "main":
settings.init()
s_size = settings.screen_size

font_path = os.path.join(settings.main_path, 'res', 'kaiti.ttf')
game = Board(screen_size=s_size, font_path=font_path)
# game = Board(screen_size=settings.screen_size)

game.add_game_state("title", Title(board=game))
game.add_game_state("start", Game(board=game))

# start game things
game.set_game_state("title")

game.run_main_loop()
