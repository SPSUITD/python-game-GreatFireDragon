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
        self.crt_filter.use()
        self.crt_filter.clear()

        self.hoop.draw()
        self.active_fruits.draw()
        self.fruit_list.draw()

        self.window.use()
        self.clear()
        self.crt_filter.draw()
            

    
    self.cursor_sprite.draw()   # должен быть последним!


