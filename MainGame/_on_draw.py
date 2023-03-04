# modules
import arcade
from static.constants import *
from GeneralModule import draw_gradient_bg

def on_draw(self):
    
    if self.on_pause:               # если пауза
        self.clear()
        self.shapes.draw()
        self.manager.draw()
    else:
        if self.filter_on:
            self.crt_filter.use()
            self.crt_filter.clear()

            self.hoop.draw()
            self.fruit_list.draw()
        self.window.use()
        self.clear()
        if self.filter_on:
            self.crt_filter.draw()
        else:
            self.hoop.draw()
            self.fruit_list.draw()

    
    self.cursor_sprite.draw()   # должен быть последним!


