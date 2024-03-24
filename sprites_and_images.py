import pygame
from abc import ABC, abstractmethod

sprite_sheet_image = pygame.image.load("smg_spritesheet.png")
sprite_bg_color = (51, 0, 51)


class Actor(ABC):
    def __init__(self, width, height, pos_x, pos_y, scale=1, color=sprite_bg_color):
        self.sprite = pygame.Surface((width, height)).convert_alpha()
        self.sprite.blit(sprite_sheet_image, (0, 0), (pos_x, pos_y, width, height))
        self.sprite = pygame.transform.scale(
            self.sprite, (width * scale, height * scale)
        )
        self.sprite.set_colorkey(color)

    def get_resting_state(self) -> pygame.Surface:
        return self.sprite


class Squid(Actor):
    width = 16
    height = 16

    def __init__(self):
        self.sprite_states: list[pygame.Surface] = []
        calc_width = lambda sprite_num: (2 * (sprite_num + 1)) + (
            Squid.width * sprite_num
        )
        for s in range(7):
            sprite = pygame.Surface((Squid.width, Squid.height)).convert_alpha()
            sprite.blit(sprite_sheet_image, (0, 0), (2, 2, calc_width(s), Squid.height))
            self.sprite_states.append(sprite)

    def get_resting_state(self):
        return self.sprite_states[0]


class Zapfish(Actor):
    width = 16
    height = 16

    def __init__(self):
        super().__init__(Zapfish.width, Zapfish.height, 20, 22)


class Crab(Actor):
    width = 16
    height = 16

    def __init__(self):
        super().__init__(Crab.width, Crab.height, 38, 22)


class Starfish(Actor):
    width = 16
    height = 16

    def __init__(self):
        super().__init__(Starfish.width, Starfish.height, 56, 22)


class Jellyfish(Actor):
    width = 16
    height = 16

    def __init__(self):
        super().__init__(Jellyfish.width, Jellyfish.height, 74, 22)


class GreenFish(Actor):
    width = 16
    height = 16

    def __init__(self):
        super().__init__(GreenFish.width, GreenFish.height, 92, 22)


class RedFish(Actor):
    width = 16
    height = 16

    def __init__(self):
        super().__init__(RedFish.width, RedFish.height, 128, 22)


class Background:
    sprite_width = 240
    sprite_height = 240

    def __init__(self, screen_width: int, screen_height: int):
        self.background = pygame.Surface((Background.sprite_width, Background.sprite_height))

        self.background.blit(
            sprite_sheet_image,
            (0, 0),
            (2, 126, Background.sprite_width, Background.sprite_height),
        )

        self.background = pygame.transform.scale(self.background, (screen_width, screen_height))

    def get_background(self) -> pygame.Surface:
        return self.background
