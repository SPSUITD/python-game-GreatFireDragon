# modules
import arcade
import random
from static.constants import *
from GeneralModule import respawn_fruit, add_fruit_to_physics_engine
width, height = arcade.window_commands.get_display_size()   # Window height and width


def on_update(self, delta_time):

    if self.on_pause:
        pass
    else:

        fruits_at_hoop = arcade.get_sprites_at_point(self.hoop.position, self.fruit_list)
        if len(fruits_at_hoop)>0:
            print(f"fruit at hoop!")
            # self.fruit_list.pop()

        self.physics_engine.step()

# Если фрукт is OOB → 
        random_index = random.randrange(0, len(self.fruit_list))
        for i in range(len(self.active_fruits)):
            if self.active_fruits[i].position[1] < random.randrange(-500, -200):

                self.physics_engine.remove_sprite(self.active_fruits[i])
                self.fruit_list.append(self.active_fruits[i])
                self.active_fruits.pop(i)
                
                self.active_fruits.append(self.fruit_list[random_index])
                self.fruit_list.pop(random_index)
                add_fruit_to_physics_engine(self, self.active_fruits[-1])

                respawn_fruit(self, self.active_fruits[-1])





                

