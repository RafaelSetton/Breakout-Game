from math import sin, cos, radians
from setton.matematica import limite  # https://github.com/RafaelSetton/setton/blob/master/matematica.py
from random import randint
import pygame
pygame.init()


class Ball:
    def __init__(self, screen: pygame.Surface):
        self.SIZE = 20
        self.screen = screen
        self.x = (self.screen.get_width() - self.SIZE) / 2
        self.y = self.screen.get_height() - 50
        self.center = (self.x + self.SIZE / 2, self.y + self.SIZE / 2)

        self.direction = randint(210, 330)
        self.x_vel = cos(radians(self.direction))
        self.y_vel = sin(radians(self.direction))

    def move(self):
        multiplier = 5
        self.x += self.x_vel * multiplier
        self.y += self.y_vel * multiplier

        if self.x > self.screen.get_width() - self.SIZE:
            self.x -= (self.x - self.screen.get_width()) * 2
            self.update_direction(180 - self.direction)
        elif self.x < 0:
            self.x -= self.x * 2
            self.update_direction(180 - self.direction)
        elif self.y < 0:
            self.y -= self.y * 2
            self.bounce_vertical()
        self.center = (self.x + self.SIZE / 2, self.y + self.SIZE / 2)

    def update_direction(self, new_direction):
        self.direction = new_direction % 360 if self.direction >= 0 else (new_direction % 360) + 360

        if abs(90 - self.direction) < 10:
            self.direction += 15 * (self.direction - 90) / abs(self.direction - 90) if (self.direction - 90) else 15
        elif self.direction < 180:
            self.direction = limite(150, 30, self.direction)
        else:
            self.direction = limite(330, 210, self.direction)

        self.x_vel = cos(radians(self.direction))
        self.y_vel = sin(radians(self.direction))

    def bounce_vertical(self):
        self.update_direction(randint(-20, 20) - self.direction)

    def bounce_horizontal(self):
        self.update_direction(randint(-15, 15) + 180 - self.direction)

    def blit(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (int(self.x), int(self.y)), int(self.SIZE / 2))
