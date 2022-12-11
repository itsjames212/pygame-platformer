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

    def run(self):
        #level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.bottom1Tile.draw(self.display_surface)

        #level player
        self.player.update()
        self.player.draw(self.display_surface)
        