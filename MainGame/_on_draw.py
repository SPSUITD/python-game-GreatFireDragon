# modules
import arcade
from static.constants import *

def on_draw(self):
    self.clear()
    self.scene.draw()


    self.cursor_sprite.draw()   # должен быть последним!


