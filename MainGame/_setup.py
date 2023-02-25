# modules
import arcade
import os
import random
from static.constants import *



def setup(self):
    self.held_fruits = []
    self.held_fruits_original_position = []

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

    # BIG FRUITS
    path = "fruits/"
    dir_list = os.listdir(path)
    for i in dir_list: 
        fruit = arcade.Sprite(f"{path}{i}")
        # fruit.center_x = random.randrange(50, SCREEN_WIDTH-50)
        fruit.center_x = random.normalvariate(SCREEN_WIDTH/2, SCREEN_WIDTH/4)
        fruit.center_y = random.normalvariate(SCREEN_HEIGHT/4, SCREEN_HEIGHT/4)
        fruit.scale = 0.3
        self.fruit_list.append(fruit)



    # COLLISION TESTS
    test_fruit = arcade.Sprite("fruits/orange.png")
    test_fruit.center_x = SCREEN_WIDTH/2
    test_fruit.center_y = SCREEN_HEIGHT/2
    self.fruit_list.append(test_fruit)
    

    # HOOP
    self.hoop.center_x = SCREEN_WIDTH/1.1
    self.hoop.center_y = SCREEN_HEIGHT/1.2
    self.hoop.scale = HOOP_SCALE


    # PHISICS ENGINE
    damping = DEFAULT_DAMPING
    gravity = (0, -GRAVITY)
    self.physics_engine = arcade.PymunkPhysicsEngine(damping=damping, gravity=gravity)

    # ADD FRUITS TO PHYSICS ENGINE
    for i in range(len(self.fruit_list)):
        self.physics_engine.add_sprite(self.fruit_list[i],
                                        friction=FRUIT_FRICTION,
                                        mass=FRUIT_MASS,
                                        moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
                                        collision_type="player",
                                        max_horizontal_velocity=FRUIT_MAX_HORIZONTAL_SPEED,
                                        max_vertical_velocity=FRUIT_MAX_VERTICAL_SPEED)

        self.physics_engine.apply_impulse(self.fruit_list[i], (0, 1000))










