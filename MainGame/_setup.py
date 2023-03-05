# modules
import arcade
import os
import random
from static.constants import *
from GeneralModule import add_fruit_to_physics_engine



def setup(self):
    self.held_fruits = []

# LITTLE 16x16 FRUITS FROM STARDEW VALLEY
    # for i in range(3):
    #     for j in range(10):
    #         for k in range(10):
    #             try:
    #                 fruit = arcade.Sprite(f"images/tile{i}{j}{k}.png")
    #                 fruit.center_x = SCREEN_WIDTH / 2
    #                 fruit.center_y = 2
    #                 fruit.scale = 6
    #                 self.fruit_list.append(fruit)
    #             except Exception: break

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
        fruit.center_y = 300
        fruit.scale = FRUIT_SCALE
        self.fruit_list.append(fruit)
          

    # HOOP
    self.hoop.center_x = SCREEN_WIDTH/1.1
    self.hoop.center_y = SCREEN_HEIGHT/1.5
    self.hoop.scale = 2*FS
    self.physics_engine.add_sprite(self.hoop,
                                    body_type = self.physics_engine.STATIC,
                                    collision_type="hoop")

    

    add_fruit_to_physics_engine(self, self.fruit_list[-1])
    self.active_fruits.append(self.fruit_list[-1])
    self.fruit_list.pop(-1)



    # COLLISION HANDLERS
    def fruit_hoop_handler(fruit, hoop, _arbiter, _space, _data):
        # self.physics_engine.remove_sprite(fruit)
        # respawn_fruit(self, fruit)
        print("fruit and hoop collide")

    self.physics_engine.add_collision_handler("fruit", "hoop", post_handler=fruit_hoop_handler)

    











