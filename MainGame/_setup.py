# modules
import arcade
import random
from static.constants import *
from ._controls import *



def setup(self):
    # Read in the tiled map
    TILE_SCALING = 1

    # Name of map file to load
    map_name = "maps/introduction.json"
    layer_options = {
            "Tile Layer 1": {
                "use_spatial_hash": True,
            },
        }

    self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)
    self.scene = arcade.Scene.from_tilemap(self.tile_map)

    # Set the background color
    if self.tile_map.background_color:
        arcade.set_background_color(self.tile_map.background_color)




