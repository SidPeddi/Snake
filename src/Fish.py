import pygame
import random
from Snake import Snake
from ScoreBoard import ScoreBoard

class Fish:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.image = pygame.image.load("../assets/fish.png")
        self.image = pygame.transform.scale(self.image, (20,20))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = 120
        self.y = 120
        self.is_eaten = False
        self.score = 0

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x = random.randrange(1, ((650 - 40) // 10)) * 10
        self.y = random.randrange(1, ((640 - 40) // 10)) * 10

    def hit_by(self, snake: Snake, score_board: ScoreBoard):
        fish_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        snake_rect = pygame.Rect(snake.x[0], snake.y[0], snake.width, snake.height)
        if fish_rect.colliderect(snake_rect):
            score_board.increment_score()
        return fish_rect.colliderect(snake_rect)

    def eaten(self):

        self.is_eaten = True
