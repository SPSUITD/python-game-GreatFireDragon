# modules
import arcade
import arcade.gui
import json
f = open("static/controls.json")
data = json.load(f)
from static.constants import *
from GeneralModule import cursor_coordinates, cursor_on_hover




from basicControls import on_mouse_basic_press, on_mouse_basic_release, on_mouse_basic_motion, on_mouse_basic_enter, on_mouse_basic_leave, on_key_basic_press, on_key_basic_release

# CONTROLS -----------------------------------------------------
def on_mouse_press(self, x, y, button, key_modifiers):
    on_mouse_basic_press(self, x, y, button, key_modifiers)

def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
    on_mouse_basic_release(self, x, y, button, modifiers)

def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
    on_mouse_basic_motion(self, x, y, dx, dy)

def on_mouse_enter(self, x, y):
    on_mouse_basic_enter(self, x, y)

def on_mouse_leave(self, x, y):
    on_mouse_basic_leave(self, x, y)

def on_key_press(self, symbol, modifiers):
    on_key_basic_press(self, symbol, modifiers)

def on_key_release(self, symbol, modifiers):
    on_key_basic_release(self, symbol, modifiers)
# CONTROLS -----------------------------------------------------