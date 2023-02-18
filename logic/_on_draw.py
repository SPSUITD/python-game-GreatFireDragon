# modules
import arcade
from Card import Card
from logic._constants import *

def on_draw(self):
    self.clear()
    self.card_list.draw()
    self.cursor_sprite.draw()

    print(self.cursor_sprite.position)

    