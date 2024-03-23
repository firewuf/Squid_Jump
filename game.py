import pygame
import sprites

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Images/Sprites
sprite_sheet_image = pygame.image.load("smg_spritesheet.png")

main_char_width = 16
main_char_height = 16


def run_game():
    pygame.init()

    screen: pygame.Surface = screen_config()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()


def screen_config() -> pygame.Surface:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Squid Jump")
    return screen


if __name__ == "__main__":
    run_game()
