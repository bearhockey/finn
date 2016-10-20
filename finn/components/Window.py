import pygame

import finn.Color as Color
from finn.components.Box import Box
from finn.Scene import Scene


class Window(object):
    def __init__(self, position, size, name=None, scene=None, border_color=Color.white):
        self.name = name
        self.position = position
        self.canvas = pygame.Surface(size=size)
        self.border = Box(pygame.Rect(position[0], position[1], size[0], size[1]),
                          box_color=None,
                          border_color=border_color,
                          highlight_color=border_color,
                          active_color=border_color)
        self.scene = scene

    def create_scene(self):
        self.scene = Scene()
        return self.scene

    def scene_change(self, new_scene):
        self.scene = new_scene
        return self.scene

    def add_component_to_scene(self, component):
        if self.scene:
            if component not in self.scene.components:
                self.scene.components.append(component)
        else:
            raise Exception("Window has no current scene.")

    def add_sprite_to_scene(self, sprite):
        if self.scene:
            if sprite not in self.scene.sprites:
                self.scene.sprites.append(sprite)
        else:
            raise Exception("Window has no current scene.")

    def update(self, key, mouse, offset=None):
        if offset is None:
            offset = self.position
        self.scene.always()
        if self.border.check_mouse_inside(mouse, (0, 0)):
            self.scene.update(key, mouse, offset)

    def draw(self, screen):
        self.canvas.fill(Color.black)
        self.scene.draw(self.canvas)
        screen.blit(self.canvas, self.position)
        self.border.draw(screen)
