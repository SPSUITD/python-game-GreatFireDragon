# modules
import arcade
import arcade.gui
import json
f = open("static/controls.json")
data = json.load(f)
from static.constants import *
from GeneralModule import cursor_coordinates, cursor_hover_fruit, pull_to_top




from basicControls import on_mouse_basic_press, on_mouse_basic_release, on_mouse_basic_motion, on_mouse_basic_enter, on_mouse_basic_leave, on_key_basic_press, on_key_basic_release

# CONTROLS -----------------------------------------------------
def on_mouse_press(self, x, y, button, key_modifiers):
    on_mouse_basic_press(self, x, y, button, key_modifiers)

    fruits_at_cursor = arcade.get_sprites_at_point((x, y), self.fruit_list)
    if len(fruits_at_cursor) > 0:
        primary_fruit = fruits_at_cursor[-1]
        self.held_fruits = [primary_fruit]
        self.held_fruits_original_position = [self.held_fruits[0].position]
        pull_to_top(self, self.held_fruits[0])

def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
    on_mouse_basic_release(self, x, y, button, modifiers)
    

    if len(self.held_fruits) == 0:
        return

    self.held_fruits = []
    cursor_hover_fruit(self, x, y)


def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
    on_mouse_basic_motion(self, x, y, dx, dy)
    cursor_hover_fruit(self, x, y)

    for fruit in self.held_fruits:
        fruit.center_x += dx
        fruit.center_y += dy

def on_mouse_enter(self, x, y):
    on_mouse_basic_enter(self, x, y)

def on_mouse_leave(self, x, y):
    on_mouse_basic_leave(self, x, y)

def on_key_press(self, symbol, modifiers):
    on_key_basic_press(self, symbol, modifiers)
    if symbol == arcade.key.P:
        self.filter_on = not self.filter_on
        
def on_key_release(self, symbol, modifiers):
    on_key_basic_release(self, symbol, modifiers)
# CONTROLS -----------------------------------------------------