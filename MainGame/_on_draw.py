# modules
import arcade
from constants import *
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

        self.basket.draw()
        # self.basket.draw_hit_box([255,0,0], 3)

        self.active_fruits.draw()
        # self.active_fruits.draw_hit_boxes([255,0,0], 3)
        # self.fruit_list.draw()
        # self.power_up_list.draw()
        self.active_power_ups.draw()
        # self.power_up_list.draw_hit_boxes([255,0,0], 3)

        self.gui["timer_text"].draw()
        self.gui["score_text"].draw()

        self.fruit_pop.draw()

        self.cursor_sprite.draw()   # должен быть последним!

        self.window.use()
        self.clear()
        
        self.crt_filter.draw()
            

    


