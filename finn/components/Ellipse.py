from math import pow, sqrt, tan, pi
import pygame
import finn.Color as Color


class Ellipse(object):
    def __init__(self, position=(0, 0), x_radius=1, y_radius=1):
        self.position = position
        self.x_radius = x_radius
        self.y_radius = y_radius
        self.color = Color.white
        self.outline = 2

    def get_point(self, angle):
        if angle == 0:
            angle = 360
        rad = angle*(pi/180)
        try:
            x = (self.x_radius * self.y_radius) / sqrt(pow(self.y_radius, 2) + pow(self.x_radius, 2)*(pow(tan(rad), 2)))
        except Exception as e:
            # print e
            x = 0
        try:
            y = (self.x_radius * self.y_radius) / sqrt(pow(self.x_radius, 2) + pow(self.y_radius, 2)/pow(tan(rad), 2))
        except Exception as e:
            # print e
            y = 0

        if 90 < angle < 270:
            x = -x
        if 180 < angle < 360:
            y = -y
        return int(x)+self.position[0], int(y)+self.position[1]

    def draw(self, screen):
        box = pygame.Rect(self.position[0] - self.x_radius, self.position[1] - self.y_radius,
                          self.x_radius * 2, self.y_radius * 2)
        pygame.draw.ellipse(screen, self.color, box, self.outline)
