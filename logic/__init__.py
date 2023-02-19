# modules
import arcade
# files
import main
from Card import Card
from ._constants import *


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.card_list = None
        arcade.set_background_color(arcade.color.AMAZON)

        self.set_mouse_visible(False)
        self.cursor_sprite = None

        self.pile_mat_list = None


    from ._setup import setup
    from ._on_draw import on_draw
    from ._controls import on_mouse_press, on_mouse_release, on_mouse_motion, pull_to_top
    # Здесь основная логика