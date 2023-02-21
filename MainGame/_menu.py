# modules
import arcade
import arcade.gui
import json
f = open("static/controls.json")
data = json.load(f)
from static.constants import *
from GeneralModule import cursor_coordinates


class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        print("quit button clicked")
        arcade.exit()

class SettingsButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        print("settings button clicked")
        # arcade.exit()

class StartButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        self.scene = SCENE_GAME
