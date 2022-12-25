import pygame
import sys
from settings import *
from level import Level
from player import *

pygame.init()
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)
DEFAULT_SKY_SIZE = (1200, screen_height)


green_health = 300
red_health = 300
health_bar = pygame.image.load('assets/health bar.png')





# game loop area
while True:
  screen.fill('black')
  health_red = pygame.draw.rect(screen, 'red', (0, 0, red_health, 40))
  health_green = pygame.draw.rect(screen, 'green', (0, 0, green_health, 40))
  screen.blit(health_bar, (0, 0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  
  
  level.run()
  pygame.display.flip()
  pygame.display.update()
  clock.tick(60)
