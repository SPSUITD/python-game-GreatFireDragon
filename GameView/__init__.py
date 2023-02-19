# modules
import arcade
# files
from Card.__init__ import Card
from InstructionView.__init__ import InstructionView
from static.constants import *


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.AMAZON)

        self.window.set_mouse_visible(False)
        self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", 1)
    
        # self.main_theme_sound = arcade.load_sound("sounds/carolOfTheBells.mp3")
        # self.main_theme_player = self.main_theme_sound.play()
        # self.main_theme_sound.set_volume(0.1, self.main_theme_player)


    from ._setup import setup
    from ._on_draw import on_draw
    from ._controls import on_mouse_press, on_mouse_release, on_mouse_motion, pull_to_top
    # Здесь основная логика