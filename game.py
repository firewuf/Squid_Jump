import pygame
import sprites_and_images as sai

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


def run_game():
    pygame.init()

    screen: pygame.Surface = screen_config()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw_game(screen)

    pygame.quit()


def draw_game(screen: pygame.Surface):
    screen.blit(sai.Background(SCREEN_WIDTH, SCREEN_HEIGHT).get_background(), (0, 0))
    pygame.display.update()


def screen_config() -> pygame.Surface:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Squid Jump")
    return screen


if __name__ == "__main__":
    run_game()
