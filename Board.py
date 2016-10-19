import pygame

import Color
from State import State


class Board(object):
    def __init__(self, screen_size=(640, 480), font_path=None):
        self.run_game = True
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode(self.screen_size)
        if font_path is None:
            font_path = pygame.font.match_font(pygame.font.get_default_font())
        self.big_font = pygame.font.Font(font_path, 48)
        self.font = pygame.font.Font(font_path, 24)
        self.small_font = pygame.font.Font(font_path, 12)

        mouse_button = {"LEFT": 1,
                        "MIDDLE": 2,
                        "RIGHT": 3,
                        "WHEEL_UP": 4,
                        "WHEEL_DOWN": 5}

        self.mouse = {mouse_button["LEFT"]: 0,
                      mouse_button["MIDDLE"]: 0,
                      mouse_button["RIGHT"]: 0,
                      mouse_button["WHEEL_UP"]: 0,
                      mouse_button["WHEEL_DOWN"]: 0}
        self.game_states = {"quit": Quit(self)}
        self.game_state = None

    def add_game_state(self, name, state):
        if name not in self.game_states:
            self.game_states[name] = state

    def set_game_state(self, name):
        if name not in self.game_states:
            raise Exception("State '{0}' is not in list of valid game states.".format(name))
        else:
            self.game_state = name

    def run_main_loop(self):
        while self.run_game:
            self.clock.tick(60)
            key_pressed = None
            unicode_pressed = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    key_pressed = event.key
                    unicode_pressed = event.unicode
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse[event.button] = 1
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse[event.button] = 0
            # update state
            state = self.game_states[self.game_state]
            state.update(key=(key_pressed, unicode_pressed), mouse=self.mouse)
            # figure out drawing shit
            self.screen.fill(Color.black)
            state.draw(self.screen)
            pygame.display.flip()


class Quit(State):
    def __init__(self, board):
        super(Quit, self).__init__(board)

    def update(self, key=None, mouse=None):
        self.board.run_game = False
