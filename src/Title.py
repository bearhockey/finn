import pygame

import Color
from State import State
from src.components.Box import Box
from src.components.text.TextBox import TextBox


class Title(State):
    def __init__(self, board, image=None, music=None):
        super(Title, self).__init__(board)
        self.screen_size = board.screen_size
        self.font = board.font
        self.title_image = None
        if image:
            self.add_title(pygame.image.load(image))
        if music:
            pygame.mixer.music.load(music)

        screen_width = self.screen_size[0]
        screen_height = self.screen_size[1]
        self.new_game = TextBox(rect=pygame.Rect(screen_width/2-40, screen_height/2+20, 120, 30),
                                highlight_color=Color.gray,
                                active_color=Color.blue,
                                name="new",
                                message="New Game",
                                text_color=Color.white,
                                text_outline=True,
                                font=self.font,
                                highlight_text=True,
                                highlight_box=False)
        self.load_game = TextBox(rect=pygame.Rect(screen_width/2-40, screen_height/2+60, 120, 30),
                                 highlight_color=Color.gray,
                                 active_color=Color.blue,
                                 name="load",
                                 message="Load Game",
                                 text_color=Color.white,
                                 text_outline=True,
                                 font=self.font,
                                 highlight_text=True,
                                 highlight_box=False)
        self.options = TextBox(rect=pygame.Rect(screen_width/2-40, screen_height/2+100, 100, 30),
                               highlight_color=Color.gray,
                               active_color=Color.blue,
                               name="options",
                               message="Options",
                               text_color=Color.white,
                               text_outline=True,
                               font=self.font,
                               highlight_text=True,
                               highlight_box=False)
        self.quit = TextBox(rect=pygame.Rect(screen_width/2-40, screen_height/2+140, 80, 30),
                            highlight_color=Color.gray,
                            active_color=Color.blue,
                            name="quit",
                            message='Quit',
                            text_color=Color.white,
                            text_outline=True,
                            font=self.font,
                            highlight_text=True,
                            highlight_box=False)
        self.buttons = [self.new_game, self.load_game, self.options, self.quit]

    @staticmethod
    def play_title_music():
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()

    @staticmethod
    def stop_title_music():
        pygame.mixer.music.fadeout(500)

    def add_title(self, title_image):
        self.title_image = Box(rect=pygame.Rect(10, 10, self.screen_size[0]-20, self.screen_size[1]-20),
                               border_color=Color.white,
                               highlight_color=Color.white,
                               active_color=Color.white,
                               border=4,
                               image=title_image)

    def update(self, key, mouse):
        name = None
        for button in self.buttons:
            if button.update(key=key, mouse=mouse):
                name = button.name
        if name == "new":
            self.board.set_game_state("start")
        if name == "quit":
            self.board.set_game_state("quit")

    def draw(self, screen):
        if self.title_image:
            self.title_image.draw(screen)
        self.new_game.draw(screen)
        self.load_game.draw(screen)
        self.options.draw(screen)
        self.quit.draw(screen)
