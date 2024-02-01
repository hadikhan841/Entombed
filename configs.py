# Tiles
import pygame.font

pygame.font.init()

TILESIZE = 64


# Screen
screen_width, screen_height = 1500, 800
play_width = 20 * TILESIZE
play_height = TILESIZE * 10


FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DIMMEDYELLOW = (189, 186, 49) #Classic ! :)) Color of the walls from the original Entombed

# Fonts
sidebar_font = pygame.font.SysFont("comicsans", 40)

# camera configs
camera_velocity = 0.125

# In-Game values
make_breaks = 3


# Maze Related variables
maze_length = 110
