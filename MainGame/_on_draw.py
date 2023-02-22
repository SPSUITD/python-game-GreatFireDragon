# modules
import arcade
from static.constants import *

def on_draw(self):
    self.clear()
    # left, screen_width, bottom, screen_height = self.window.get_viewport()
    self.tile_map.sprite_lists["PixelCatsFree"].draw()


    self.cursor_sprite.draw()   # должен быть последним!


