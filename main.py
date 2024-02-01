import pygame, os, csv
from configs import *
from mazegenerator import generate_random_bit
from sprites import *

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()

# Constant variables
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Entombed by Hadi")

# Groups
wall_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
make_group = pygame.sprite.Group()

camera_group = CameraGroup()


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load("Assets/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2()

        self.speed = 1

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.direction.x = 0

        elif keys[pygame.K_DOWN] and self.rect.bottom <= (
            -1 * camera_group.offset.y + screen_height
        ):
            self.direction.y = 1
            self.direction.x = 0

        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.direction.y = 0

        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.direction.y = 0

        else:
            self.direction.x = 0
            self.direction.y = 0

    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, wall_group, False)
            if hits:
                if self.vel.x > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width

                if self.vel.x < 0:
                    self.rect.x = hits[0].rect.right

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, wall_group, False)
            if hits:
                if self.vel.y > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height

                if self.vel.y < 0:
                    self.rect.y = hits[0].rect.bottom

    def update(self):
        keys = pygame.key.get_pressed()
        self.input()
        self.collide_blocks("x")
        self.collide_blocks("y")
        self.vel = self.direction * self.speed
        self.rect.center += self.vel


player = Player((500, 400), camera_group)
player_group.add(player)

# Read the csv file and create walls based on 1 values inside3 the file
def create_tilemap():
    with open("Assets/maze.csv", "r") as maze:
        reader = csv.reader(maze)
        for i, line in enumerate(reader):
            for j, c in enumerate(line):
                if c == "1":
                    wall = Wall(j, i, camera_group)
                    wall_group.add(wall)
                if c == "2":
                    make = Make(j, i, camera_group)
                    make_group.add(make)


def generate_maze():
    import mazegenerator


def reset():
    pass


# All the Drawings will be done here
def draw(screen, camera_group):
    generate_maze()
    screen.fill(BLACK)

    # draw the camera group containig walls in it
    wall_group.update()

    camera_group.update()
    camera_group.custom_draw()

    # Texts
    make_text = sidebar_font.render(f"Makes: {make_breaks}", 1, WHITE)
    make_text_rect = make_text.get_rect()
    make_text_rect.center = (screen_width - 140, 20)
    screen.blit(make_text, make_text_rect)

    pygame.display.update()


def main():
    global make_breaks

    run = True
    clock.tick(FPS)  # FPS = 60
    create_tilemap()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()  # from os library

            # Destroying walls
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE) and (make_breaks > 0):
                    if pygame.sprite.groupcollide(
                        player_group, wall_group, False, True
                    ):
                        make_breaks -= 1

        if player.rect.y < -1 * camera_group.offset.y:

            reset()

        if pygame.sprite.groupcollide(player_group, make_group, False, True):
            make_breaks += 1
        camera_group.offset -= (0, camera_velocity)
        draw(screen, camera_group)

# Running the project
if __name__ == "__main__":
    main()
