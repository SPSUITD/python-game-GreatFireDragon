# modules
import arcade
import arcade.gui
from arcade.experimental.uislider import UISlider
from static.constants import *
import json

f = open("static/controls.json")
data = json.load(f)

width, height = arcade.window_commands.get_display_size()   # Window height and width


class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()

def create_buttons(self):
    self.v_box = arcade.gui.UIBoxLayout()

    quit_button = QuitButton(text="Quit", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, style=MENU_STYLE)
    self.v_box.add(quit_button.with_space_around(bottom=BUTTON_MARGIN))

    self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="center_y", child=self.v_box))