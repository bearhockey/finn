import Color
from State import State


class Game(State):
    def __init__(self, board):
        super(Game, self).__init__(board)
        self.add_window(name="main", properties={"position": (50, 50),
                                                 "size": (100, 200),
                                                 "name": "main",
                                                 "border_color": Color.white})
