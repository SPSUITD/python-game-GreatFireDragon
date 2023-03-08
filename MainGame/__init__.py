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
                                    display_warp = Vec2(1.0 / 32.0, 1.0 / 18.0),
                                    mask_dark=0.5, mask_light=1.5)
        self.filter_on = False
        
        # OBJECTS
        self.fruit_list = arcade.SpriteList(use_spatial_hash=False)
        self.active_fruits = arcade.SpriteList(use_spatial_hash=False)
        self.hoop = arcade.Sprite("images/basket.png", hit_box_algorithm='Detailed', hit_box_detail=4.5)

        # костыль для удобного удаления объектов из массивов
        self.removed_from_engine = False
            
        # CURSOR
        self.window.set_mouse_visible(False)

        self.cursor_sprite = arcade.Sprite()
        define_cursor(self)

        #  MANAGER
        self.manager = arcade.gui.UIManager()

        # DRAG AND DROP
        self.held_fruits = arcade.SpriteList(use_spatial_hash=False)
        self.cursor_delta = [1,1]
        self.mouse_is_pressed = False


        # PHYSICS ENGINE
        self.physics_engine = arcade.PymunkPhysicsEngine
        self.on_pause = False


        # TIMER & SCORE
        self.gui = {
            "timer": 1.0,
            "timer_text": arcade.Text(
                                text="00:00:00",
                                start_x= 100*FS,
                                start_y= 50*FS,
                                color=arcade.color.ORANGE_PEEL,
                                font_size=FONT_SIZE*2,
                                anchor_x="center",
                            ),
            "score": 0
        }
        


    
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
    from ._pause_menu import on_click_get_back, on_click_menu
    # Здесь основная логика


