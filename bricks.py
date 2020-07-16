import pygame
pygame.init()


class Bricks:
    def __init__(self, screen: pygame.Surface):
        self.colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255)]
        self.screen = screen
        self.bricks = list(self.create())

    def blit(self):
        def once(color, x, y):
            pygame.draw.rect(self.screen, color, ((x, y), (70, 40)))

        for brick in self.bricks:
            once(*brick)

    def create(self):
        ini_x = 20
        ini_y = 30
        dif_x = (self.screen.get_width() - 20) / 9
        dif_y = 50
        for l in range(5):
            for c in range(10):
                yield (self.colors[l], ini_x + c * dif_x, ini_y + l * dif_y)
