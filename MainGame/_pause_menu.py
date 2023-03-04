# modules
import arcade
import arcade.gui
from arcade.experimental.uislider import UISlider

from GeneralModule import get_back_button_create
from static.constants import *

import json
f = open("static/controls.json")
data = json.load(f)

width, height = arcade.window_commands.get_display_size()   # Window height and width


class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.close_window()

def create_buttons(self):
    self.v_box = arcade.gui.UIBoxLayout()

    get_back_button_create(self)

    menu_button = arcade.gui.UIFlatButton(text="Back To Menu", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, style=MENU_STYLE)
    self.v_box.add(menu_button.with_space_around(bottom=BUTTON_MARGIN))
    menu_button.on_click = self.on_click_menu

    quit_button = QuitButton(text="Quit", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, style=MENU_STYLE)
    self.v_box.add(quit_button.with_space_around(bottom=BUTTON_MARGIN))

    self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="center_y", child=self.v_box))

def on_click_get_back(self, event):
    self.v_box.clear()
    self.on_pause = not self.on_pause
    self.manager.enable() if self.on_pause else self.manager.disable()

def on_click_menu(self, event):
    self.on_pause = not self.on_pause
    self.manager.enable() if self.on_pause else self.manager.disable()
    
    self.manager.clear()
    from Menu import Menu
    view = Menu()
    self.window.show_view(view)