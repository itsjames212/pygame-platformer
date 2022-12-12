import pygame
from tiles import Tile
from settings import tile_size
from player import Player
from tiles import Bottom1

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.bottom1Tile = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for column_index, cell in enumerate(row):
                x = column_index * tile_size
                y = row_index * tile_size

                if cell == 'T':
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                if cell == 'X':
                    tile2 = Bottom1((x,y), tile_size)
                    self.bottom1Tile.add(tile2)


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
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom









    def run(self):
        #level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.bottom1Tile.draw(self.display_surface)

        #level player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)