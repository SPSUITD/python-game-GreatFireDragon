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


    from ._setup import setup
    from ._on_draw import on_draw
    from ._controls import on_key_press, on_key_release
    from ._camera import center_camera_to_player
    # Здесь основная логика
    from ._update import update