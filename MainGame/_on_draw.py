# modules
import arcade
from static.constants import *
from GeneralModule import draw_gradient_bg

def on_draw(self):
    
    if self.on_pause:               # если пауза
        self.clear()
        self.shapes.draw()
        self.manager.draw()

        self.cursor_sprite.draw()   # должен быть последним!
    else:
        self.crt_filter.use()
        self.crt_filter.clear()

        self.hoop.draw()
        self.hoop.draw_hit_box([255,0,0], 3)

        self.active_fruits.draw()
        self.active_fruits.draw_hit_boxes([255,0,0], 3)
        self.fruit_list.draw()

        self.gui["timer_text"].draw()
        self.cursor_sprite.draw()   # должен быть последним!

        self.window.use()
        self.clear()
        
        self.crt_filter.draw()
            

    


