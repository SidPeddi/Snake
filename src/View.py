import pygame
from Game import Game


# TODO: Put your names here (entire team)


class View:
    def __init__(self, screen: pygame.Surface, game: Game):
        self.screen = screen
        self.game = game



    def draw_everything(self):
        # self.screen.fill(self.background_color)
        self.game.draw_game()  # Implement draw_game in your Game class
        pygame.display.update()


