# modules
import arcade
import random
from static.constants import *
from GeneralModule import respawn_fruit, add_fruit_to_physics_engine, swap_fruit_index
width, height = arcade.window_commands.get_display_size()   # Window height and width


def on_update(self, delta_time):

    if self.on_pause:
        pass
    else:

        # fruits_at_hoop = arcade.get_sprites_at_point(self.hoop.position, self.active_fruits)
        # if len(fruits_at_hoop)>0:
        #     print(f"fruit at hoop!")
        #     # self.fruit_list.pop()

        self.physics_engine.step()

# Если фрукт is OOB → 
    for i in range(len(self.active_fruits)):
        if self.active_fruits[i].position[1] < random.randrange(-500, -200):
            swap_fruit_index(self, i)




                

