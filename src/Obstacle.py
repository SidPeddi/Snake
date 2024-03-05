import pygame
import random
from Snake import Snake
class Obstacle:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.image = pygame.image.load("../assets/rock.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = 280
        self.y = 280


    def move(self):
        self.x = random.randrange(1, ((650 - 40) // 10)) * 10
        self.y = random.randrange(1, ((640 - 40) // 10)) * 10

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def hit_by(self, snake: Snake):
        obstacle_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        snake_rect = pygame.Rect(snake.x[0], snake.y[0], snake.width, snake.height)
        if obstacle_rect.colliderect(snake_rect):
            snake.die()
        return obstacle_rect.colliderect(snake_rect)

