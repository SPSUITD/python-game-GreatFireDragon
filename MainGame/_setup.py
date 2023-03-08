# modules
import arcade
import os
import random
from static.constants import *
from GeneralModule import add_fruit_to_physics_engine



def setup(self):
    # PHISICS ENGINE
    damping = DEFAULT_DAMPING
    gravity = (0, -GRAVITY)
    self.physics_engine = arcade.PymunkPhysicsEngine(damping=damping, gravity=gravity)

 # BIG FRUITS
    fruit_path = "fruits/"
    dir_list = os.listdir(fruit_path)

    for i in dir_list: 
        fruit = arcade.Sprite(f"{fruit_path}{i}")
        # fruit.center_x = random.randrange(50, SCREEN_WIDTH-50)
        fruit.center_x = random.normalvariate(SCREEN_WIDTH/2, SCREEN_WIDTH/4)
        fruit.center_y = -200
        fruit.scale = FRUIT_SCALE
        self.fruit_list.append(fruit)
          

    # HOOP
    self.hoop.center_x = SCREEN_WIDTH/1.3
    self.hoop.center_y = SCREEN_HEIGHT/1.5
    self.hoop.scale = 2*FS

    
    # ADDING FRUITS to physics engine
    add_fruit_to_physics_engine(self, self.fruit_list[-1])
    self.active_fruits.append(self.fruit_list[-1])
    self.fruit_list.pop(-1)

    add_fruit_to_physics_engine(self, self.fruit_list[-1])
    self.active_fruits.append(self.fruit_list[-1])
    self.fruit_list.pop(-1)

    add_fruit_to_physics_engine(self, self.fruit_list[-1])
    self.active_fruits.append(self.fruit_list[-1])
    self.fruit_list.pop(-1)



    # COLLISION HANDLERS (ATAVISM)
    # def fruit_hoop_handler(fruit, hoop, _arbiter, _space, _data):
    #     # self.physics_engine.remove_sprite(fruit)
    #     # respawn_fruit(self, fruit)
    #     print("fruit and hoop collide")

    # self.physics_engine.add_collision_handler("fruit", "hoop", post_handler=fruit_hoop_handler)














