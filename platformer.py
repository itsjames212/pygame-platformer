import pygame, sys
from settings import *
from level import Level

pygame.init()
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)
sky = pygame.image.load('pygameassets/skybackground.png')
DEFAULT_SKY_SIZE = (1200, screen_height)
sky = pygame.transform.scale(sky, DEFAULT_SKY_SIZE)

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