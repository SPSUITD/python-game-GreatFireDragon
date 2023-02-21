# modules
import arcade
from static.constants import *

def on_draw(self):
    self.clear()
    left, screen_width, bottom, screen_height = self.get_viewport()

    # if self.scene == SCENE_MENU:
    #     self.manager.draw()
    #     self.cursor_sprite.draw()   # должен быть последним!
    # elif self.scene == SCENE_GAME:
    self.cursor_sprite.draw()   # должен быть последним!


