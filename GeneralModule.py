import arcade
import arcade.gui
from pyglet.math import Vec2
from static.constants import *

width, height = arcade.window_commands.get_display_size()   # Window height and width

def cursor_coordinates(self, x, y):
    if self.window.fullscreen:        
        x = ( x / width ) * SCREEN_WIDTH
        y = ( y / height ) * SCREEN_HEIGHT
    self.cursor_sprite.center_x = x
    self.cursor_sprite.center_y = y

def is_cursor_hover_fruit(self, x, y):
    fruits_at_cursor = arcade.get_sprites_at_point((x, y), self.fruit_list)
    cursor_N = 0
    if len(self.held_fruits) == 0:         # Если мы ничего не держим
        cursor_N = 1 if len(fruits_at_cursor) > 0 else 2 if self.mouse_is_pressed else 0
    else:
        cursor_N = 2

    self.cursor_sprite.set_texture(cursor_N)
    cursor_coordinates(self, x, y)

# В ситуации, когда мы кликнули на объект, который находистя позади 
# другого объекта. Мы хотим, чтобы кликнутый нами "активный" объект
# окахался наверху. Это приятнее для восприятия.
def pull_to_top(self, fruit: arcade.Sprite):
        self.fruit_list.remove(fruit)
        self.fruit_list.append(fruit)
