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
        fruit_at_hoop = arcade.get_sprites_at_point(self.hoop.position, self.held_fruits)
        # print(self.fruit_list)
        if len(fruit_at_hoop)>0:
            self.held_fruits.pop()
            fruit_at_hoop[0].set_position(-200, random.randrange(200, 1000))
            
            self.physics_engine.add_sprite(fruit_at_hoop[0])

        self.physics_engine.step()

        # Если фрукт Out Of Bounds(OOB)
        for i in range(len(self.active_fruits)):
            if self.active_fruits[i].position[1] < random.randrange(-500, -200):
                swap_fruit_index(self, i)




                

