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
        if fruit.position[1] < 0:
            # fruit.center_y = SCREEN_HEIGHT/2
            # self.physics_engine.set_position(fruit, (random.normalvariate(SCREEN_WIDTH/2, SCREEN_WIDTH/3), SCREEN_HEIGHT+100))
            # self.physics_engine.resync_sprites()
            if random.random() > 0.9:
                self.physics_engine.apply_impulse(fruit, (random.randrange(-100, 100), random.randrange(1000, 2000)))

        if fruit.position[0] < 0 or fruit.position[0] > SCREEN_WIDTH:
            # fruit.center_y = SCREEN_HEIGHT/2
            self.physics_engine.set_position(fruit, (random.normalvariate(SCREEN_WIDTH/2, SCREEN_WIDTH/4), 
                                                    random.normalvariate(SCREEN_HEIGHT/4, SCREEN_HEIGHT/4)))
            # self.physics_engine.resync_sprites()



            

