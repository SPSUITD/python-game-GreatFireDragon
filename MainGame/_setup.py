# modules
import arcade
import os
import random
from static.constants import *
from GeneralModule import add_fruit_to_physics_engine, teleport_basket



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
          

    # basket
    teleport_basket(self)
    self.basket.scale = 0.1*FS

    
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

    # POWER-UPs
    self.power_ups.append(arcade.Sprite("images/arrow.png"))
    self.power_ups.append(arcade.Sprite("images/x2.png"))
    self.power_ups.append(arcade.Sprite("images/clock.png"))
    for power_up in self.power_ups:
        power_up.scale = POWER_UP_SCALE

    self.power_ups[0].center_x = SCREEN_WIDTH//2
    self.power_ups[0].center_y = SCREEN_HEIGHT//2

    # EFFECTS
    self.fruit_pop.set_position(self.basket.position[0], self.basket.position[1])
    self.fruit_pop.scale = 0.3
    self.fruit_pop.set_texture(33)



    # COLLISION HANDLERS (ATAVISM)
    # def fruit_basket_handler(fruit, basket, _arbiter, _space, _data):
    #     # self.physics_engine.remove_sprite(fruit)
    #     # respawn_fruit(self, fruit)
    #     print("fruit and basket collide")

    # self.physics_engine.add_collision_handler("fruit", "basket", post_handler=fruit_basket_handler)














