import pygame, sys
from pygame.locals import QUIT
import random

WIDTH = 900
HEIGHT = 500
FPS = 60

pygame.init
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('game')
clock = pygame.time.Clock()

def openWindowLoop():
  running = True
  while running:
    clock.tick(FPS)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
  pygame.display.flip()
  pygame.quit()
openWindowLoop()
