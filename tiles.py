import pygame
from foldergrab import *


class Grass(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('assets/grass.png')
        DEFAULT_GROUND_SIZE = ((size, size))
        self.image = pygame.transform.scale(self.image, DEFAULT_GROUND_SIZE)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Dirt(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('assets/dirt.png')
        DEFAULT_GROUND_SIZE = ((size, size))
        self.image = pygame.transform.scale(self.image, DEFAULT_GROUND_SIZE)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Rightcorner(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('assets/rightcorner.png')
        DEFAULT_GROUND_SIZE = ((size, size))
        self.image = pygame.transform.scale(self.image, DEFAULT_GROUND_SIZE)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Leftcorner(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('assets/leftcorner.png')
        DEFAULT_GROUND_SIZE = ((size, size))
        self.image = pygame.transform.scale(self.image, DEFAULT_GROUND_SIZE)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
