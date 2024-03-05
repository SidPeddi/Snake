import pygame
import sys

from Fish import Fish
from Obstacle import Obstacle
from Snake import Snake
from ScoreBoard import ScoreBoard

# ISHII Daichi, Siddarth Peddi, Tulsi C Manohar
pygame.init()
crashed_sound = pygame.mixer.Sound("../assets/crash.wav")
eat_sound = pygame.mixer.Sound("../assets/ding.wav")
pygame.font.init()

class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.fish = Fish(self.screen)
        self.obstacle = Obstacle(self.screen)
        self.snake = Snake(self.screen)
        self.scoreboard = ScoreBoard(self.screen)


    def draw_game(self):
        """ Ask all the objects in the game to draw themselves. """
        self.fish.draw()
        self.snake.draw()
        self.scoreboard.draw()
        self.obstacle.draw()
    def draw_endgame(self):
        self.snake.draw()


    def run_one_cycle(self):
        """ All objects that do something at each cycle: ask them to do it. """
        if (self.fish.hit_by(self.snake, self.scoreboard)):
            self.fish.move()
            self.obstacle.move()
            self.fish.eaten()
            self.snake.grow()
            pygame.mixer.Sound.play(eat_sound)
        if (self.obstacle.hit_by(self.snake)):
            self.snake.die()
            self.scoreboard.reset()
        if self.snake.length >= 11:
            pygame.display.set_caption("You Won!!")
            if self.snake.length >= 12:
                self.scoreboard.reset()
                self.snake.is_alive = False

        if self.snake.is_alive == False:
            pygame.mixer.Sound.play(crashed_sound)
            pygame.mixer.music.stop()

    def game_over(self):
        if self.snake.is_alive == False:
            pygame.display.set_caption("Game over")
            return True
        else:
            return False



