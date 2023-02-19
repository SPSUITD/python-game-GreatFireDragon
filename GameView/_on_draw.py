# modules
import arcade
from Card.__init__ import *
from static import constants

def on_draw(self):
    self.clear()
    
    self.cursor_sprite.draw()   # должен быть последним!

    