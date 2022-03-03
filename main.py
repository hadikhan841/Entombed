import pygame, sys, csv
from configs import *
from tiles import *

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()

# Constant variables
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Entombed")

wall_group = pygame.sprite.Group()


# Read the csv file and create files based on 1 values inside3 the file
def create_tilemap():
    with open('Assets/maze.csv', 'r') as maze:
        reader = csv.reader(maze)
        for i, line in enumerate(reader):
            for j, c in enumerate(line):
                if c == '1':
                    wall = Wall(j, i)
                    wall_group.add(wall)


# All the Drawings will process here
def draw(screen, wall_group):
    wall_group.draw(screen)

    # Texts
    level_text = sidebar_font.render('Level: 0', 1, WHITE)
    level_text_rect = level_text.get_rect()
    level_text_rect.center = (screen_width - 140, 20)
    screen.blit(level_text, level_text_rect)

    health_text = sidebar_font.render('Health: 3', 1, WHITE)
    health_text_rect = level_text.get_rect()
    health_text_rect.center = (screen_width - 140, 80)
    screen.blit(health_text, health_text_rect)

    make_text = sidebar_font.render('Makes: 3', 1, WHITE)
    make_text_rect = level_text.get_rect()
    make_text_rect.center = (screen_width - 140, 140)
    screen.blit(make_text, make_text_rect)

    pygame.display.update()


def main():
    run = True
    clock.tick(FPS)
    create_tilemap()
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()


        draw(screen, wall_group)


if __name__ == "__main__":
    main()
