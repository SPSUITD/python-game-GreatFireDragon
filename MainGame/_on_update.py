# modules
import arcade
from static.constants import *


def on_update(self, delta_time):
    fruits_at_hoop = arcade.get_sprites_at_point(self.hoop.position, self.fruit_list)
    if len(fruits_at_hoop)>0:
        print(f"fruit at hoop!")
        self.fruit_list.pop()