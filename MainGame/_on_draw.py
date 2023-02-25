# modules
import arcade
from static.constants import *

def on_draw(self):

    if self.filter_on:
        self.crt_filter.use()
        self.crt_filter.clear()

        self.hoop.draw()
        self.fruit_list.draw()
        self.cursor_sprite.draw()   # должен быть последним!
    self.window.use()
    self.clear()
    if self.filter_on:
        self.crt_filter.draw()
    else:
        self.hoop.draw()
        self.fruit_list.draw()
        self.cursor_sprite.draw()   # должен быть последним!


