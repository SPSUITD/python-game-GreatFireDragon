# modules
import arcade
import arcade.gui
import json
f = open("static/controls.json")
data = json.load(f)
# files
from static.constants import *
from ._menu import StartButton, SettingsButton, QuitButton

class  MainGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=data["fullscreen"])
        self.scene = SCENE_MENU
        arcade.set_background_color(arcade.color.AMAZON)

        #  GUI START -----------------------------------------------------------
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Buttons
        self.v_box = arcade.gui.UIBoxLayout()

        start_button = StartButton(text="Start Game", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))

        settings_button = SettingsButton(text="Settings", width=200)
        self.v_box.add(settings_button.with_space_around(bottom=20))

        quit_button = QuitButton(text="Quit", width=200)
        self.v_box.add(quit_button.with_space_around(bottom=20))

        self.manager.add(
            arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="center_y", child=self.v_box)
            )
        #  GUI END -------------------------------------------------------------

        # CURSOR
        self.set_mouse_visible(False)
        self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", 1)
    
        # SOUNDS
        # self.main_theme_sound = arcade.load_sound("sounds/carolOfTheBells.mp3")
        # self.main_theme_player = self.main_theme_sound.play()
        # self.main_theme_sound.set_volume(0.1, self.main_theme_player)


    

    from ._setup import setup
    from ._on_draw import on_draw
    from ._controls import on_mouse_press, on_mouse_release, on_mouse_motion, on_mouse_enter, on_mouse_leave, on_key_press, on_key_release
    # Здесь основная логика