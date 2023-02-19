# modules
import arcade
from Card import Card
from logic._constants import *

def on_draw(self):
    self.clear()
    self.pile_mat_list.draw()
    self.card_list.draw()
    # должен быть последним!
    self.cursor_sprite.draw()

    