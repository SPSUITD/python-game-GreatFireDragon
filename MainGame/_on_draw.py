# modules
import arcade
from static.constants import *

def on_draw(self):

    if self.filter_on:
        self.crt_filter.use()
        self.crt_filter.clear()

        self.sprite_list.draw()
        self.cursor_sprite.draw()   # должен быть последним!

        self.window.use()
        self.clear()
        self.crt_filter.draw()
    else:
        self.window.use()
        self.clear()
        
        self.sprite_list.draw()
        self.cursor_sprite.draw()


