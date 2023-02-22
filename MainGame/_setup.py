# modules
import arcade
import random
from static.constants import *
from ._controls import *



def setup(self):
    # Read in the tiled map
    TILE_SPRITE_SCALING = 0.5
    self.tile_map = arcade.load_tilemap(
        "maps/introduction.json", scaling=TILE_SPRITE_SCALING
    )

    # Set the background color
    if self.tile_map.background_color:
        arcade.set_background_color(self.tile_map.background_color)




