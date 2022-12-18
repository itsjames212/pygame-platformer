import pygame, sys
from settings import *
from level import *
from player import *
from tiles import *

pygame.init()
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)
sky = pygame.image.load('pygameassets/backgroundimage.png')
DEFAULT_SKY_SIZE = (1200, screen_height)
sky = pygame.transform.scale(sky, DEFAULT_SKY_SIZE)

scroll = [0, 0]







#open loop area
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    
  screen.blit(sky,(0, 0))
  level.run()
  pygame.display.flip()
  pygame.display.update()
  clock.tick(60)