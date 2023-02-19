# modules
import arcade
# files
import main
from Card.__init__ import *
from InstructionView.__init__ import *
from static.constants import *


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.AMAZON)

        self.window.set_mouse_visible(False)
        self.cursor_sprite = None


    from ._setup import setup
    from ._on_draw import on_draw
    from ._controls import on_mouse_press, on_mouse_release, on_mouse_motion, pull_to_top
    # Здесь основная логика