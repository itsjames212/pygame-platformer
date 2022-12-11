import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('pygameassets/groundsprite.png')
        DEFAULT_GROUND_SIZE = ((size, size))
        self.image = pygame.transform.scale(self.image, DEFAULT_GROUND_SIZE)
        self.rect = self.image.get_rect(topleft = pos)


    def update(self, x_shift):
        self.rect.x += x_shift