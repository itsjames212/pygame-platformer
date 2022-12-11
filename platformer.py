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
#player area
player = pygame.image.load('pygameassets/playerimage.png')
x = 600
y = 500
velocity = 12

#open loop area
while True:
  screen.blit(player,(x, y))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
          x -= velocity
      if event.key == pygame.K_RIGHT:
          x += velocity
      if event.key == pygame.K_UP:
          y -= velocity
      if event.key == pygame.K_DOWN:
          y += velocity
  screen.blit(sky,(0, 0))
  level.run()
  pygame.display.flip()
  pygame.display.update()
  clock.tick(60)