#PYGAME BOILER PLATE
import pygame, sys
from pygame.locals import QUIT
import random

width = 900
height = 500
FPS = 60
rect_color = (255, 255, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('game')
clock = pygame.time.Clock()

def drawWindow():
  pygame.draw.rect(screen, rect_color, pygame.Rect(1, 210, 3, 85))
  pygame.draw.rect(screen, rect_color, pygame.Rect(895, 210, 3, 85))

  pygame.display.update()

#loop to keep the screen open until x clicked
def openWindowLoop():
  running = True
  while running:
    clock.tick(FPS)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      drawWindow()
  pygame.display.flip()
  pygame.quit()
openWindowLoop()