# modules
import arcade
import arcade.gui
import json
# files
from static.constants import *

class  MainGame(arcade.View):

    def __init__(self):
        super().__init__()
        arcade.set_background_color(BG_MAINGAME)
        
        # CURSOR
        self.window.set_mouse_visible(False)
        self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", 1)

    
        # SOUNDS
        # self.main_theme_sound = arcade.load_sound("sounds/HARDCORE!!!.mp3")
        # self.main_theme_player = self.main_theme_sound.play()
        # f = open("static/controls.json")
        # data = json.load(f)
        # self.main_theme_sound.set_volume(data["volume"], self.main_theme_player)

    
    from ._setup import setup
    from ._on_draw import on_draw
    from ._controls import on_mouse_press, on_mouse_release, on_mouse_motion, on_mouse_enter, on_mouse_leave, on_key_press, on_key_release
    # Здесь основная логика