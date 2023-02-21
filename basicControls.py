import arcade
import json
f = open("static/controls.json")
data = json.load(f)

from static.constants import *
from GeneralModule import cursor_coordinates, cursor_on_hover



def on_mouse_basic_press(self, x, y, button, key_modifiers):
    self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_3.png", 1)
    cursor_coordinates(self, x, y)

def on_mouse_basic_release(self, x: float, y: float, button: int, modifiers: int):
    self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", 1)
    cursor_coordinates(self, x, y)

def on_mouse_basic_motion(self, x: float, y: float, dx: float, dy: float):
    cursor_coordinates(self, x, y)

def on_mouse_basic_enter(self, x, y):
    self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", 1)
    cursor_coordinates(self, x, y)

def on_mouse_basic_leave(self, x, y):
    pass

def on_key_basic_press(self, symbol, modifiers):
    # f11 для смены режима fullscreen
    if symbol == 65480:
        self.window.set_fullscreen(not self.window.fullscreen)
        data["fullscreen"] = self.window.fullscreen                    # Также запись состояния в JSON
        with open("static/controls.json", "w") as jsonFile:     # чтобы было удобно
            json.dump(data, jsonFile)

        self.window.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)    # чтобы растянуть на весь экран


def on_key_basic_release(self, symbol, modifiers):
    pass


