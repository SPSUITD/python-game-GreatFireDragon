# modules
import arcade
from arcade.experimental.crt_filter import CRTFilter
from pyglet.math import Vec2
from arcade.experimental import Shadertoy
import json
# files
from static.constants import *
from GeneralModule import define_cursor

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
        
        # OBJECTS
        self.fruit_list = arcade.SpriteList(use_spatial_hash=True)
        self.hoop = arcade.Sprite("images/hoop.png", hit_box_algorithm='Detailed')
        self.removed = False
            
        # CURSOR
        self.window.set_mouse_visible(False)

        self.cursor_sprite = arcade.Sprite()
        define_cursor(self)

        #  MANAGER
        self.manager = arcade.gui.UIManager()

        # DRAG AND DROP
        self.held_fruits = None
        self.cursor_delta = [1,1]
        self.mouse_is_pressed = False


        # PHYSICS ENGINE
        self.physics_engine = arcade.PymunkPhysicsEngine
        self.on_pause = False

        # CREATE BUTTONS
        from ._pause_menu import create_buttons
        create_buttons(self)

    
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


