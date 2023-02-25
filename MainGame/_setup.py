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
        fruit = arcade.Sprite(f"{path}{i}", hit_box_detail=3, hit_box_algorithm='Simple')
        # fruit.center_x = random.randrange(50, SCREEN_WIDTH-50)
        fruit.center_x = random.normalvariate(SCREEN_WIDTH/2, SCREEN_WIDTH/4)
        fruit.center_y = 50
        fruit.scale = 0.3
        self.fruit_list.append(fruit)

    # HOOP
    self.hoop.center_x = SCREEN_WIDTH/1.1
    self.hoop.center_y = SCREEN_HEIGHT/1.2
    self.hoop.scale = HOOP_SCALE



