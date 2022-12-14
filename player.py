import pygame
from settings import *
from level import *
from tiles import *
from foldergrab import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.importCharacterAssets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 1
        self.gravity = 0.8
        self.jump_speed = -18

        # player status
        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction.x = 5
            self.facing_right = True
        elif keys[pygame.K_a]:
            self.direction.x = -5
            self.facing_right = False
        elif keys[pygame.MOUSEBUTTONDOWN]:
            self.status = 'attack'
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.direction.y == 0:
            self.jump()

    def importCharacterAssets(self):
        character_path = 'graphics/character/'
        self.animations = {
            'idle': [],
            'run': [],
            'jump': [],
            'fall': [],
            'attack': []
        }
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_character(full_path)

    def animate(self):
        animation = self.animations[self.status]

        # looping frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]

        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

        # set the rect
        if self.on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)
        else:
            self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()
