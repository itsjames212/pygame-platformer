import pygame
import sys
from settings import *
from level import Level
from player import *

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)
DEFAULT_SKY_SIZE = (1200, screen_height)

green_health = 300
white = (255, 255, 255)
red_health = 300
health_bar = pygame.image.load('assets/health bar.png')
x = 1000
y = 10


font = pygame.font.Font('freesansbold.ttf', 16)
fps = clock
# set the center of the rectangular object.



# game loop area
while True:
    clock.tick(60)
    screen.fill('black')
    text = font.render(f'{clock}', True, white)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    level.run()
    health_red = pygame.draw.rect(screen, 'red', (0, 0, red_health, 40))
    health_green = pygame.draw.rect(screen, 'green', (0, 0, green_health, 40))
    screen.blit(health_bar, (0, 0))
    pygame.display.flip()
    pygame.display.update()
    
