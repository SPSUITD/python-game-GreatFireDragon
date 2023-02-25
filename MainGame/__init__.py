# modules
import arcade
import random
from arcade.experimental.crt_filter import CRTFilter
from pyglet.math import Vec2
from arcade.experimental import Shadertoy
import json
import os
# files
from static.constants import *

class  MainGame(arcade.View):

    def __init__(self):
        super().__init__()
        arcade.set_background_color(BG_MAINGAME)

        # CRT filter
        self.crt_filter = CRTFilter(SCREEN_WIDTH, SCREEN_HEIGHT,
                                    resolution_down_scale=3.0,
                                    hard_scan=-8.0, hard_pix=-3.0,
                                    display_warp = Vec2(1.0 / 8.0, 1.0 / 8.0),
                                    mask_dark=0.5, mask_light=1.5)
        self.filter_on = False

        self.fruit_list = arcade.SpriteList()
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
            fruit.center_x = random.randrange(50, SCREEN_WIDTH-50)
            fruit.center_y = 50
            fruit.scale = 0.3
            self.fruit_list.append(fruit)
            
        # CURSOR
        self.window.set_mouse_visible(False)
        self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", CURSOR_SCALE)


        # DRAG AND DROP
        self.held_fruits = []
        self.held_fruits_original_position = []

    
        # SOUNDS
        # self.main_theme_sound = arcade.load_sound("sounds/HARDCORE!!!.mp3")
        # self.main_theme_player = self.main_theme_sound.play()
        # f = open("static/controls.json")
        # data = json.load(f)
        # self.main_theme_sound.set_volume(data["volume"], self.main_theme_player)

    
    from ._setup import setup
    from ._on_update import on_update
    from ._on_draw import on_draw
    from ._controls import on_mouse_press, on_mouse_release, on_mouse_motion, on_mouse_enter, on_mouse_leave, on_key_press, on_key_release
    # Здесь основная логика