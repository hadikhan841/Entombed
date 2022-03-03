import pygame
from configs import *


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
