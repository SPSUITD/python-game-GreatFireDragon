# modules
import arcade
import random
from static.constants import *


def on_update(self, delta_time):

    

    fruits_at_hoop = arcade.get_sprites_at_point(self.hoop.position, self.fruit_list)
    if len(fruits_at_hoop)>0:
        print(f"fruit at hoop!")
        # self.fruit_list.pop()

    self.physics_engine.step()

    for fruit in self.fruit_list:
        if fruit.position[1] < 50:
            self.physics_engine.set_position(fruit, (random.normalvariate(SCREEN_WIDTH/2, SCREEN_WIDTH/4), 100))
            self.physics_engine.set_velocity(fruit, (random.randrange(-100, 100), FRUIT_IMPULSE ))

        if fruit.position[0] < 0 or fruit.position[0] > SCREEN_WIDTH:
            self.physics_engine.set_position(fruit, (random.normalvariate(SCREEN_WIDTH/2, SCREEN_WIDTH/4), 100))
            self.physics_engine.set_velocity(fruit, (random.randrange(-FRUIT_MAX_HORIZONTAL_SPEED/2, FRUIT_MAX_VERTICAL_SPEED/2), FRUIT_IMPULSE ))





            

