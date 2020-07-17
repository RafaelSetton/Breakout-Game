import pygame
from time import sleep
ball = __import__('ball')
paddle = __import__('paddle')
bricks = __import__('bricks')
pygame.init()


class Game:
    def __init__(self):
        self.tela: pygame.Surface = pygame.display.set_mode((800, 650))
        self.ball = ball.Ball(self.tela)
        self.paddle = paddle.Paddle(self.tela)
        self.bricks = bricks.Bricks(self.tela)
        self.running = True
        self.live = True
        self.keys_pressed = set()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.live = False
            elif event.type == pygame.KEYDOWN:
                self.keys_pressed.add(event.key)
            elif event.type == pygame.KEYUP:
                try:
                    self.keys_pressed.remove(event.key)
                except KeyError:
                    pass
        for key in self.keys_pressed:
            if key == pygame.K_LEFT:
                self.paddle.move(-1)
            elif key == pygame.K_RIGHT:
                self.paddle.move(1)
        self.paddle_handler()
        self.bricks_handler()
        if self.ball.y > self.tela.get_height():
            self.live = False

    def paddle_handler(self):
        pd: paddle.Paddle = self.paddle
        collisions = [self.ball.collision(pd.y, pd.y + pd.height, pd.x),
                      self.ball.collision(pd.y, pd.y + pd.height, pd.x + pd.width),
                      self.ball.collision(pd.x, pd.x + pd.width, y=pd.y)]
        if any(collisions[:2]):
            self.ball.bounce_horizontal()
        if collisions[2]:
            self.ball.bounce_vertical()

    def bricks_handler(self):
        for brick in self.bricks.bricks:
            brick_x, brick_y = brick[1:]
            brick_width, brick_height = 70, 40
            collisions = [self.ball.collision(brick_y, brick_y + brick_height, brick_x),
                          self.ball.collision(brick_y, brick_y + brick_height, brick_x + brick_width),
                          self.ball.collision(brick_x, brick_x + brick_width, y=brick_y),
                          self.ball.collision(brick_x, brick_x + brick_width, y=brick_y + brick_height)]
            if any(collisions):
                if any(collisions[:2]):
                    self.ball.bounce_horizontal()
                if any(collisions[2:]):
                    self.ball.bounce_vertical()
                self.bricks.bricks.remove(brick)

    def new_game(self):
        fonte = pygame.font.SysFont('Agency FB', 60)\
            .render("Aperte qualquer tecla para continuar", True, (255, 255, 255))
        self.tela.blit(fonte, (int(self.tela.get_width() / 2 - 350), int(self.tela.get_height() / 2 - 50)))
        pygame.display.update()
        while True:
            events = [event for event in pygame.event.get() if event.type in (pygame.KEYDOWN, pygame.QUIT)]
            if [event for event in events if event.type == pygame.QUIT]:
                self.running = False
                self.live = False
                break
            if [event for event in events if event.type == pygame.KEYDOWN]:

                self.keys_pressed = {event.key for event in events if event.type == pygame.KEYDOWN}
                self.live = True
                self.ball = ball.Ball(self.tela)
                self.bricks = bricks.Bricks(self.tela)
                break


game = Game()
while game.running:
    game.new_game()
    while game.live:
        game.tela.fill((0, 0, 0))

        game.ball.move()
        game.ball.blit()
        game.paddle.blit()
        game.bricks.blit()

        pygame.display.update()
        game.event_handler()
        sleep(0.01)
