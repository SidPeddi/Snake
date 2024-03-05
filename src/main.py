import pygame
from Game import Game
from Controller import Controller
from View import View
from Snake import Snake



# ISHII Daichi, Siddarth Peddi, Tulsi C Manohar
pygame.init()
eat_sound = pygame.mixer.Sound("../assets/ding.wav")

def button(screen, position, text):
    screen.fill("white")
    font = pygame.font.SysFont("Comicsansms", 50)
    text_render = font.render(text, 1, (255, 255, 255))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 10)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 10)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 10)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 10)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w, h))
    return screen.blit(text_render, (x, y))


def start():
    screen = pygame.display.set_mode((640, 650))
    image1 = pygame.image.load("../assets/background.jpg")  #
    clock = pygame.time.Clock()
    game = Game(screen)  # the Model
    viewer = View(screen, game)  # the View
    controller = Controller(game)  # the Controller
    snake = Snake(screen)
    frame_rate = 60
    while True:
        clock.tick(frame_rate)
        controller.get_and_handle_events()
        image1 = pygame.transform.scale(image1,(640,650))
        screen.blit(image1,(0,0))
        game.run_one_cycle()
        viewer.draw_everything()  # Includes the pygame.display.update()
        if game.game_over() == True:
            screen.fill("black")
            b2 = button(screen, (205, 230), "Play Again")
            while True:
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT):
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                        key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                        if key_to_start:
                            main()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if b2.collidepoint(pygame.mouse.get_pos()):
                            main()
                pygame.display.update()
            pygame.quit()
            viewer.draw_everythingendgame()  # Includes the pygame.display.update()

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 650))
    pygame.display.set_caption("Underwater Snake")  # Done: Choose your own title
    b1 = button(screen, (255, 230), "Start")
    image1 = pygame.image.load("../assets/background.jpg")  #
    clock = pygame.time.Clock()

    frame_rate = 60
    while True:
        pygame.mixer.music.load("../assets/Main Theme.wav")
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(-1)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                if key_to_start:
                    start()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    start()
        pygame.display.update()
    pygame.quit()

main()



