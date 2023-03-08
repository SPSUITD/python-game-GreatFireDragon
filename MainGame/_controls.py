# modules
import arcade
import arcade.gui
import json
f = open("static/controls.json")
data = json.load(f)
from static.constants import *
from GeneralModule import cursor_coordinates, is_cursor_hover_fruit, draw_gradient_bg

width, height = arcade.window_commands.get_display_size()   # Window height and width


from basicControls import on_mouse_basic_press, on_mouse_basic_release, on_mouse_basic_motion, on_mouse_basic_enter, on_mouse_basic_leave, on_key_basic_press, on_key_basic_release

# CONTROLS -----------------------------------------------------
def on_mouse_press(self, x, y, button, key_modifiers):
    on_mouse_basic_press(self, x, y, button, key_modifiers)

    fruits_at_cursor = arcade.get_sprites_at_point((x, y), self.active_fruits) # error with fullscren so different method
    if len(fruits_at_cursor) > 0:
        primary_fruit = fruits_at_cursor[-1]

        if not self.removed_from_engine:
            self.physics_engine.remove_sprite(primary_fruit)
            # primary_fruit.scale = FRUIT_HELD_SCALE
            self.removed_from_engine = True


        self.held_fruits.append(primary_fruit)
        self.held_fruits[0].turn_right(self.held_fruits[0].angle)
    else:
        self.mouse_is_pressed = True

def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
    on_mouse_basic_release(self, x, y, button, modifiers)
    self.mouse_is_pressed = False

    if len(self.held_fruits) == 0:
        return

    # self.held_fruits[0].scale = FRUIT_SCALE
    if self.removed_from_engine:
        self.physics_engine.add_sprite(self.held_fruits[0])
        self.removed_from_engine = False
    self.physics_engine.apply_impulse(self.held_fruits[0], list(map(lambda x: x * 50, self.cursor_delta)))

    # print("fruit angle:", self.held_fruits[0].angle)

    self.held_fruits.pop()
    is_cursor_hover_fruit(self, x, y)


def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
    on_mouse_basic_motion(self, x, y, dx, dy)
    is_cursor_hover_fruit(self, x, y)

    for fruit in self.held_fruits:
        fruit.center_x += dx
        fruit.center_y += dy

    # if self.window.fullscreen:        
    #     dx = ( dx / width ) * SCREEN_WIDTH
    #     dy = ( dy / height ) * SCREEN_HEIGHT
    self.cursor_delta = [dx, dy]    # Чтобы в on_mouse_release можно было передать фрукту какую-то скорость
    

def on_mouse_enter(self, x, y):
    on_mouse_basic_enter(self, x, y)

def on_mouse_leave(self, x, y):
    on_mouse_basic_leave(self, x, y)

def on_key_press(self, symbol, modifiers):
    on_key_basic_press(self, symbol, modifiers)
    if symbol == arcade.key.P:
        self.filter_on = not self.filter_on
    if symbol == arcade.key.ESCAPE:
        draw_gradient_bg(self)
        from ._pause_menu import create_buttons
        create_buttons(self)
        self.on_pause = not self.on_pause
        self.manager.enable() if self.on_pause else self.manager.disable()

    if symbol == arcade.key.L and modifiers & arcade.key.MOD_SHIFT:
        self.gui["timer"] = 0
    if symbol == arcade.key.K and modifiers & arcade.key.MOD_SHIFT:
        self.gui["score"] = 420
        
    if symbol == arcade.key.UP:
        print("presed: UP")
    if symbol == arcade.key.DOWN:
        print("pressed: DOWN")
    
        
def on_key_release(self, symbol, modifiers):
    on_key_basic_release(self, symbol, modifiers)
# CONTROLS -----------------------------------------------------