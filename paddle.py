from setton.matematica import limite  # https://github.com/RafaelSetton/setton/blob/master/matematica.py
import pygame
pygame.init()


class Paddle:
    def __init__(self, screen: pygame.Surface):
        self.width = 80
        self.height = 20

        self.screen = screen
        self.x = (self.screen.get_width() - self.width) / 2
        self.y = self.screen.get_height() - 30

    def move(self, direction):
        self.x = limite(self.screen.get_width() - self.width, 0, self.x + 6 * direction)

    def blit(self):
        pygame.draw.rect(self.screen, (200, 0, 255), ((self.x, self.y), (self.width, self.height)))
        new_y = self.y + self.height / 2
        pygame.draw.line(self.screen, (0, 0, 0), (self.x + 10, new_y), (self.x + self.width - 10, new_y), 2)
