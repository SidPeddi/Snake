import pygame
from ScoreBoard import ScoreBoard
class Snake:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.speed = 3
        self.is_alive = True
        self.is_hit = False
        self.length = 1
        self.x = [10]
        self.y = [10]
        self.image = pygame.image.load("../assets/snakebody.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.heading = "right"
        self.width = 20
        self.height = 20

    def draw(self):
        for k in range(self.length):
            self.screen.blit(self.image, (self.x[k], self.y[k]))


    def move_left(self):
        for k in range(self.length -1, 0, -1):
            self.x[k] = self.x[k-1]
            self.y[k] = self.y[k-1]
        self.x[0] -= self.speed
        self.heading = "left"
        if self.x[0] <= -20:
            self.die()


    def move_right(self):
        for k in range(self.length -1, 0, -1):
            self.x[k] = self.x[k-1]
            self.y[k] = self.y[k-1]
        self.x[0] += self.speed
        self.heading = "right"
        if self.x[0] >= 650:
            self.die()


    def move_up(self):
        for k in range(self.length -1,0,-1):
            self.x[k] = self.x[k-1]
            self.y[k] = self.y[k-1]
        self.y[0] -= self.speed
        self.heading = "up"
        if self.y[0] <= -20:
            self.die()


    def move_down(self):
        for k in range(self.length-1,0,-1):
            self.x[k] = self.x[k-1]
            self.y[k] = self.y[k-1]
        self.y[0] += self.speed
        self.heading = "down"
        if self.y[0] >= 640:
            self.die()


    def grow(self):
        self.x += [self.x[self.length -1] -20]
        self.y += [self.y[self.length -1]]
        self.length += 1
        self.speed += 0.1



    def die(self):
        self.x = [10]
        self.y = [10]
        self.length = 1
        self.speed = 0
        self.is_alive = False
