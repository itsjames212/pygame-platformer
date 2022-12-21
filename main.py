import pygame
import sys
from settings import *
from player import *

pygame.init()
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
DEFAULT_SKY_SIZE = (1200, screen_height)


def load_map(path):
    f = open(path + '.txt', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map


game_map = load_map('pygameassets/map')

ground_image = pygame.image.load('pygameassets/newground.png')

# game loop area
while True:
    for layer in game_map:
        tile_rects = []
        y = 0
        for tile in layer:
            x = 0
            if tile == 'X':
                screen.blit(ground_image, (x * 16, y * 16))
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            x += 1
        y += 1

        def __init__(self, pos, size):
            self.image = ground_image
            DEFAULT_GROUND_SIZE = ((size, size))
            self.image = pygame.transform.scale(
                self.image, DEFAULT_GROUND_SIZE)
            self.rect = self.image.get_rect(topleft=pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
