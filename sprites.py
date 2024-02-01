import pygame
from configs import *


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, group):
        super().__init__(group)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.start_maze_location = 10
        self.width = TILESIZE
        self.height = TILESIZE

        # Wall Image
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(DIMMEDYELLOW)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # camera offset
        self.offset = pygame.math.Vector2()

    def custom_draw(self):
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft + self.offset
            self.display_surface.blit(sprite.image, offset_pos)


class Make(pygame.sprite.Sprite):
    def __init__(self, x, y, group):
        super().__init__(group)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.start_maze_location = 10
        self.width = 32
        self.height = 32

        # Wall Image
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
