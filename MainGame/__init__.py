# modules
import arcade
import arcade.gui
import json
f = open("static/controls.json")
data = json.load(f)
# files
from static.constants import *

class  MainGame(arcade.View):

    def __init__(self):
        super().__init__()
        # This will get the size of the window, and set the viewport to match.
        # So if the window is 1000x1000, then so will our viewport. If
        # you want something different, then use those coordinates instead.
        arcade.set_background_color(BG_MAINGAME)
        self.scene = SCENE_MENU
        
        # CURSOR
        self.window.set_mouse_visible(False)
        self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", 1)
    
        # SOUNDS
        # self.main_theme_sound = arcade.load_sound("sounds/carolOfTheBells.mp3")
        # self.main_theme_player = self.main_theme_sound.play()
        # self.main_theme_sound.set_volume(0.1, self.main_theme_player)

    def set_scene(cont_scene):
        self.scene = cont_scene
    
    from ._setup import setup
    from ._on_draw import on_draw
    from ._controls import on_mouse_press, on_mouse_release, on_mouse_motion, on_mouse_enter, on_mouse_leave, on_key_press, on_key_release
    # Здесь основная логика