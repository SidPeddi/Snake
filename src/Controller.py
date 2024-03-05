import pygame
import sys
from Game import Game


# TODO: Put your names here (entire team)


class Controller:
    def __init__(self, game: Game):
        self.game = game

    def get_and_handle_events(self):
        """
        [Describe what keys and/or mouse actions cause the game to ...]
        """
        events = pygame.event.get()
        self.exit_if_time_to_quit(events)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            if self.game.snake.heading != "up":
                self.game.snake.move_up()
        if pressed_keys[pygame.K_DOWN]:
            if self.game.snake.heading != "down":
                self.game.snake.move_down()
        if pressed_keys[pygame.K_LEFT]:
            if self.game.snake.heading != "left":
                self.game.snake.move_left()
        if pressed_keys[pygame.K_RIGHT]:
            if self.game.snake.heading != "right":
                self.game.snake.move_right()

        if self.game.snake.heading == "up":
            self.game.snake.move_up()
        if self.game.snake.heading == "down":
            self.game.snake.move_down()
        if self.game.snake.heading == "left":
            self.game.snake.move_left()
        if self.game.snake.heading == "right":
            self.game.snake.move_right()


        # Use code like the following, but for YOUR Game object.
        #     if pressed_keys[pygame.K_LEFT]:
        #         self.game.fighter.move_left()
        #     if pressed_keys[pygame.K_RIGHT]:
        #         self.game.fighter.move_right()
        #
        #     if self.key_was_pressed_on_this_cycle(pygame.K_SPACE, events):
        #         self.game.fighter.fire()

    @staticmethod
    def exit_if_time_to_quit(events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

    @staticmethod
    def key_was_pressed_on_this_cycle(key, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == key:
                return True
        return False
