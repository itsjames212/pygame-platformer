import pygame
from tiles import *
from settings import tile_size
from player import Player


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for column_index, cell in enumerate(row):
                x = column_index * tile_size
                y = row_index * tile_size

                if cell == '1':
                    tile = Grass((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == '2':
                    tile2 = Dirt((x, y), tile_size)
                    self.tiles.add(tile2)
                if cell == 'R':
                    tile3 = Rightcorner((x, y), tile_size)
                    self.tiles.add(tile3)
                if cell == '3':
                    tile5 = Bottomleft((x, y), tile_size)
                    self.tiles.add(tile5)
                if cell == '4':
                    tile6 = Bottomright((x, y), tile_size)
                    self.tiles.add(tile6)
                if cell == 'L':
                    tile4 = Leftcorner((x, y), tile_size)
                    self.tiles.add(tile4)
                if cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    def run(self):
        # level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        # level player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        player_x_direction = player.direction.x

        if player_x > 1000 and player_x_direction > 0:
            player.speed = 0
            self.world_shift = -3
        elif player_x < 200 and player_x_direction < 0:
            player.speed = 0
            self.world_shift = 3
        else:
            player.speed = 1
            self.world_shift = 0
